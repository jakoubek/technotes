---
title: Bitweise Speicherung von Berechtigungen in PostgreSQL
section: postgresql
slug: bitwise
---

# Bitweise Speicherung von Berechtigungen in PostgreSQL

## Hintergrund

Bit-Werte werden oft genutzt, wenn man in Datenbanken oder Programmen mehrere verschiedene Ja/Nein-Werte **in einem Feld** speichern will. Diese verschiedenen Werte können dabei in beliebiger Kombination erscheinen.

Diese Ja/Nein-Werte (oft *Flags* oder *Switches* genannt, da sie nur "an" oder "aus" sind) stehen dann z.B. für verschiedene Berechtigungen, die ein Account haben kann.

## Umsetzung

Zur Umsetzung erstellt man sich eine Tabelle mit allen in Frage kommenden Berechtigungen. Wichtig ist, dass die Reihenfolge der einzelnen Berechtigungen festgelegt ist und bestehen bleibt. Die Logik der Reihenfolge ist indes nicht relevant, d.h. aufeinander folgende Berechtigungen müssen nicht zwingend zusammengehören.

| Lfd. Nr. | Berechtigung |
| - | :------- |
| 1 | darf Benutzer freischalten |
| 2 | darf Benutzer löschen |
| 3 | darf neue Kostenstellen anlegen |
| 4 | darf E-Mail-Konfiguration ändern |

Jetzt vergibt man jeder Berechtigung eine Bit-Nummer, wobei die Nummer sich immer als Potenz zur Basis 2 wie folgt errechnet:

```
2 ^ (laufende Nummer - 1)
```

Die Tabelle stellt sich jetzt so dar:

| Lfd. Nr. | Berechtigung | Bit-Nr. |
| - | :------- | --: |
| 1 | darf Benutzer freischalten | 1 |
| 2 | darf Benutzer löschen | 2 |
| 3 | darf neue Kostenstellen anlegen | 4 |
| 4 | darf E-Mail-Konfiguration ändern | 8 |

Da die Bit-Nummern eben keine einfach aufeinander folgenden Zahlen sind (wie es die "laufenden Nummern" wären), ist es jetzt möglich, *beliebige Kombinationen* durch einfaches Aufsummieren *in einem Wert* darzustellen.

### Beispiele

- 1 und 2 (Benutzer freischalten und Benutzer löschen) = **3** (weil Bit-Nr. 1 + 2 = 3)
- 1 und 4 (Benutzer freischalten + E-Mail-Konfiguration) = **9** (weil Bit-Nr. 1 + 8 = 9)
- keine Berechtigungen (d.h. alle Berechtigungen auf "nein" gesetzt) = **0** (weil gar keine Bits summiert werden)
- alle Berechtigungen = **15** (weil 1 + 2 + 4 + 8 = 15)

### Berechtigungen speichern

In einer Datenbank kann jetzt in der Benutzertabelle in einer Spalte (z.B. `berechtigungen`) der errechnete Wert gespeichert werden.

| ID  | USER_NAME | BERECHTIGUNGEN |
| :-- | :-------- | -------------: |
| 1   | john      | 3 |
| 2   | mary      | 9 |
| 3   | bob       | 0 |
| 4   | alice     | 15 |

### Berechtigungen erweitern

Möchte man während der Lebenszeit eines Softwaresystems die Tabelle mit Berechtigungen um neue Berechtigungen erweitern, lässt sich das ganz einfach umsetzen:

Eine neue Zeile in der Tabelle anlegen und für diese die Bit-Nummer ermitteln:

| Lfd. Nr. | Berechtigung | Bit-Nr. |
| - | :------- | --: |
| 5 | darf Massendatenexport durchführen | 16 |

## Berechtigungen prüfen

### Logik der Prüfung

Die Summe aller möglichen Berechtigungen (wenn also alle Berechtigungen auf "ja" gesetzt sind) ergibt im *Dualsystem* immer eine Zahl, die nur aus Einsen besteht. In unserem Beispiel ist die Summe aller möglichen Berechtigungen **15** - im Dualsystem ist das **1111**. Man *sieht* dieser Zahl an: jetzt sind alle Flags gesetzt (weil 1 und nicht 0). Die einzelnen Stellen dieser Dualzahl bezeichnet man als *Bits*.

Für die Prüfung, ob ein Account eine spezielle Berechtigung hat, muss jetzt prüfen, ob das entsprechende Bit gesetzt ist (also den Wert 1 hat).

Am Beispiel von *mary* aus der obigen Tabelle:

1. Sie hat die Berechtigungen 1 und 4 (Benutzer freischalten + E-Mail-Konfiguration), als Summe = 9
2. 9 als Dualzahl ergibt 1001
3. Man sieht der Dualzahl 1001 an, dass die 1. und 4. Berechtigung gesetzt ist
4. Möchte man prüfen, ob sie die Berechtigung 3 hat, muss man sich das 3. Bit anschauen, ob es gesetzt ist: in der Zahl 10**0**1 ist das 3. Bit *nicht* gesetzt - sie hat die Berechtigung "darf neue Kostenstellen anlegen" also nicht

### Beispiel

Für fast jede Programmiersprache gibt es Funktionen, Methoden, Bibliotheken, um Bitwise-Operationen durchzuführen.

Dabei ist es oft nicht einmal notwendig, die als Summe gespeicherte Berechtigung in eine Dualzahl umzuwandeln - die Funktionen können oft direkt mit den Dezimalwerten umgehen.

Allerdings verwenden die entsprechenden mathematischen Operatoren in PostgreSQL nicht die *Nummer des Feldes*, sondern den *Offset*. Das bedeutet, dass zur Prüfung, ob das erste Bit gesetzt ist, der Offset 0 und nicht die Nummer 1 verwendet werden muss.

Es bietet sich jetzt an, unsere Tabelle noch einmal um eine Spalte für den Offset zu erweitern:

| Offset | Lfd. Nr. | Berechtigung | Bit-Nr. |
| - | - | :------- | --: |
| 0 | 1 | darf Benutzer freischalten | 1 |
| 1 | 2 | darf Benutzer löschen | 2 |
| 2 | 3 | darf neue Kostenstellen anlegen | 4 |
| 3 | 4 | darf E-Mail-Konfiguration ändern | 8 |
| 4 | 5 | darf Massendatenexport durchführen | 16 |

Für die Prüfung in PostgreSQL verwendet man zwei mathematische Operatoren, die für *logische* Prüfungen im Zusammenhang mit Bits gedacht sind:

- die *bitweise Verschiebung* (*bit shift*)
- und das *bitweise UND*

### Bitweises UND

Das bitweise UND kann auf Bitzeichenfolgen *gleicher Länge* angewendet werden. Dabei wird eine Ergebnis-Zeichenfolge der gleichen Länge zurückgegeben. Bei dieser wird für jede Stelle der Eingangs-Zeichenfolgen immer dann ein gesetztes Bit (1)zurückgegeben, wenn *beide* Bits in den beiden Eingangs-Zeichenfolgen ebenfalls gesetzt sind. Andernfalls wird ein nicht gesetztes Bit (0) zurückgegeben.

| Bit 1 | Bit 2 | Ergebnis |
| :---: | :---: | :------: |
| 1     | 1     | 1        |
| 1     | 0     | 0        |
| 0     | 1     | 0        |
| 0     | 0     | 0        |

Beispiele:

```
  1001        1111        1111        1111
& 1110      & 0110      & 0000      & 1111
------      ------      ------      ------
  1000        0110        0000        1111
```

Das bitweise UND wird meistens mit einem Kaufmannsund-Zeichen (&) dargestellt.

### Bitweise Verschiebung

> Bei den bitweisen Verschiebungen werden die Bits als einzelne Zeichen an einer bestimmten Bit-Position aufgefasst – und nicht als Paare korrespondierender Bits wie in den oben stehenden Operationen.
([Wikipedia](https://de.wikipedia.org/wiki/Bitweiser_Operator#Bitweise_Verschiebungen))

Bei einer bitweisen Verschiebung werden die einzelnen Bits um eine angegebene Anzahl an Positionen nach rechts oder links verschoben.

Die bitweise Verschiebung wird meistens mit zwei spitzen Klammern nach rechts oder links dargestellt: `<<` bzw. `>>`

Für unseren Einsatzzweck wird die Berechtigungssumme dabei um den jeweiligen Offset verschoben. Möchte man also prüfen, ob die 1. Berechtigung (Offset = 0) gesetzt ist, bleibt das Ergebnis das gleiche. Wenn man den Offset erhöht, um *höhere* Berechtigungen zu prüfen, ändert sich der Wert entsprechend:


```sql
SELECT 9 >> 0;       -- 9
SELECT 9 >> 1;       -- 4
SELECT 9 >> 2;       -- 2
SELECT 9 >> 3;       -- 1
SELECT 9 >> 4;       -- 0
```

Das Wert dieser ersten Operation kann jetzt mit dem bitweisen UND kombiniert werden. Als Ergebnis bekommt man 0 oder 1, je nachdem, ob das entsprechende Bit gesetzt ist.

```sql
SELECT (9 >> 0) & 1;       -- 1 -> Berechtigung 1 ist gesetzt
SELECT (9 >> 1) & 1;       -- 0 -> Berechtigung 2 ist nicht gesetzt
SELECT (9 >> 2) & 1;       -- 0 -> Berechtigung 3 ist nicht gesetzt
SELECT (9 >> 3) & 1;       -- 1 -> Berechtigung 4 ist gesetzt
SELECT (9 >> 4) & 1;       -- 0 -> Berechtigung 5 ist nicht gesetzt
```

Wenn man spaßeshalber alle Bits in einem Rutsch prüfen und sehen möchte, kann man sich wie folgt behelfen:

```sql
WITH tmp AS
(
  SELECT 9 AS berechtigungen,
           generate_series(0, 4, 1) AS "offset"
)
SELECT  berechtigungen, "offset",
        (berechtigungen >> "offset") AS shift,
        (berechtigungen >> "offset") & 1 AS undiert
FROM    tmp;
```

| berechtigungen | offset | shift | undiert |
| -------------: | -----: | ----: | ------: |
| 9 | 0 | 9 | 1 |
| 9 | 1 | 4 | 0 |
| 9 | 2 | 2 | 0 |
| 9 | 3 | 1 | 1 |
| 9 | 4 | 0 | 0 |

## Informationen

- [Bitweiser Operator – Wikipedia](https://de.wikipedia.org/wiki/Bitweiser_Operator)
- [Bitwise magic in PostgreSQL | Medium](https://medium.com/developer-rants/bitwise-magic-in-postgresql-1a05284e4017)
- [PostgreSQL: Documentation: 14: 9.3. Mathematical Functions and Operators](https://www.postgresql.org/docs/14/functions-math.html)


{{ feedback(page.meta.title, page.meta.section, page.meta.slug) }}
