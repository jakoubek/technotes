# Stored Procedures

## Funktion vs. Prozedur

In Datenbanken können normalerweise zwei unterschiedliche Typen von *Prozeduren* angelegt werden: Funktionen und - eben - Prozeduren. Wodurch unterscheiden sich diese?

Generell handelt es sich bei Stored Procedures (SP) um "Programme", die *etwas* machen oder zurückgeben (oder beides) und die **in der Datenbank** unter einem Namen gespeichert sind und aufgerufen werden können.

### Funktionen

Eine **Funktion** ist eine SP, die **genau einen Wert** zurückgibt. "Genau ein Wert" heißt konkret: die *Ergebnistabelle* besteht aus einer Zeile mit einer Spalte.

Typischerweise können Funktionen per `SELECT`-Statement aufgerufen und so das Ergebnis abgefragt werden:

```sql
SELECT meine_funktion();

-- 4711
```

In diesem Beispiel gibt die Funktion `meine_funktion` einen Zahlenwert zurück.


### Prozeduren

Eine **Prozedur** ist eine SP, die im Gegensatz zur Funktion mehrdimensionale Werte zurückgeben kann (aber nicht muss).

Am Beispiel einer Kundentabelle könnte das Ergebnis einer Prozedur so aussehen:

| ID | KuNr  | Name   | Umsatz  |
| :--| :-----| :------| -------:|
| 1  | K1001 | BMW AG | 125.000 |
| 2  | K1002 | McDonalds | 37.500 |
| 3  | K1003 | Deutsche Bahn | 42.000 |

Der Aufruf von Prozeduren erfolgt oft über Sprachelemente wie `CALL` oder `EXEC`:

```sql
CALL kundenliste();
```

Während eine Funktion praktisch immer einen Wert zurückgibt (dafür ist sie da), *muss* die Prozedur nicht zwingend einen Rückgabewert haben. Es kann Situationen geben, dass die Prozedur in Tabellen nur Daten ändert oder anlegt. Denkbar ist aber auch die Kombination: die Prozedur ändert etwas in Tabellen und gibt ein Ergebnis aus. Dabei muss das zurückgegebene Ergebnis technisch nicht zwingend mit den geänderten Daten zu tun haben (obwohl das in der Praxis der Fall sein dürfte).

Prozeduren und Funktionen können (müssen aber nicht) Parameter entgegennehmen.



## Stored Procedure vs. Entwicklung in Programmiersprache

TODO

## Stored Procedure vs. Abfrage/View

TODO


## Use Case: Auswertung in Form einer Prozedur

Ich verwende Prozeduren gerne für komplexe Auswertungen. Die Voraussetzung für die Nutzung einer Prozedur ist natürlich immer, dass das erwartete Ergebnis Tabellenform hat.

In der Prozedur wird dabei eine sog. *lokale temporäre Tabelle* angelegt, die die Struktur der erwarteten Ergebnistabelle hat.

Die Prozedur befüllt dann diese temporäre Tabelle nach und nach mit Daten und/oder reichert diese weiter an. Im Vergleich zur einer komplexen Abfrage (s.o.) erlaubt diese Form der Datenbereitstellung später eine bessere Wartung. Es sind nicht alle Schritte in einer Abfrage untergebracht, sondern jeder Schritt ist als separater Prozedurschritt verfügbar. Anpassungen oder Erweiterungen sind meiner Erfahrung nach damit im Nachhinein einfacher und weniger fehleranfällig.

*Beispiel folgt*

