---
title: Zeilengenerator in SQL Anywhere
section: sql-anywhere
slug: zeilengenerator
---


# Zeilengenerator in SQL Anywhere

Ein Zeilengenerator ist ein Werkzeug, mit dem man eine Liste zwischen zwei beliebigen Zahlen erzeugen kann.

SQL Anywhere hat dafür eine eingebaute Systemprozedur namens *sa_rowgenerator*. 

Im folgenden Beispiel wird eine Tabelle mit den Zahlen 1 bis 10 erzeugt:

```sql
SELECT row_num FROM sa_rowgenerator(1, 10, 1);

-- 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
```

Die drei Parameter sind dabei optional und haben folgende Bedeutung:

1. Startzahl (Defaultwert: 0)
2. Endzahl (Defaultwert: 100)
3. Schrittweite (Defaultwert: 1)

Das bedeutet: ohne Parameter aufgerufen liefert die Prozedur eine Liste mit allen Zahlen von 0 bis 100.

### Schrittweite

Typischerweise möchte man *jede* Zahl zwischen den beiden "Zahlengrenzen" bekommen. Möchte man aber beispielsweise nur jede zweite Zahl haben, kann man das über den dritten Parameter steuern:

```sql
SELECT row_num FROM sa_rowgenerator(1, 10, 2);

-- 1, 3, 5, 7, 9
```

Wer nur die geraden Zahlen zwischen 1 und 10 haben will, muss dann den Startwert entsprechend auf 2 setzen:

```sql
SELECT row_num FROM sa_rowgenerator(2, 10, 2);

-- 2, 4, 6, 8, 10
```


## Beispiele

Man möchte die Monatsnummern aller Monate bekommen:

```sql
SELECT row_num FROM sa_rowgenerator(1, 12);
```

Alle Jahre zwischen 1989 und 2022:

```sql
SELECT row_num FROM sa_rowgenerator(1989, 2022);
```

Die Kombination aus beidem: für *jedes Jahr* zwischen 2019 und 2022 möchte man *für jeden Monat* einen Datensatz bekommen. Dazu muss man beide Ergebnismengen `JOIN`en. Hier im Beispiel geht das am einfachsten über eine sog. `CTE` (besser bekannt als `WITH`-Statement). Alternativ geht auch der eher konventionelle Weg über zwei Subqueries.

```sql
WITH jahre(jahr) AS (
  SELECT row_num FROM sa_rowgenerator(2019, 2022)
),
monate(monat) AS (
  SELECT row_num FROM sa_rowgenerator(1, 12)
)
SELECT jahre.jahr,
       monate.monat
FROM   jahre
       CROSS JOIN
       monate
ORDER BY jahre.jahr, monate.monat;
```

Das Ergebnis wird eine zweispaltige Tabelle mit allen Monaten von 2019-2022 sein (insgesamt also 4 x 12 = 48 Datensätze).

| jahr | monat |
| :----|-----: |
| 2019 |     1 |
| 2019 |     2 |
| 2019 |     3 |
| ...  |   ... |
| 2022 |    10 |
| 2022 |    11 |
| 2022 |    12 |


## Verwendung

Im Rahmen einer SQL-Abfrage (View, Prozedur) kann man diese generierte Ergebnistabelle zusammen mit weiteren Daten kombinieren, z.B. summierter Umsatz je Jahr oder Monat.

Wenn man nur den Umsatz nach Monat gruppiert, kann es sein, dass bei Monaten ohne Umsatz diese Zeilen komplett fehlen. Durch die Kombination mit der generierten Liste von Monatsnummern ist sichergestellt, dass für jeden Monat eine Zeile zurückgegeben wird.

Am Beispiel einer solchen fiktiven Datenbank listen wir je Monat die Summe der Umsätze auf.

```sql
SELECT  monat,
        SUM(umsatz) AS summe_umsatz
FROM    umsatztabelle
GROUP BY monat
ORDER BY monat;
```

| monat | summe_umsatz |
| :---- | -----------: |
| 1     |     3.800,00 |
| 2     |     4.500,00 |
| 3     |     4.250,00 |
| 5     |     5.100,00 |
| 6     |     4.400,00 |
| 8     |     4.750,00 |
| ...   |     .... |

Abhängig von der Datenkonstellation kann es sein, dass wir nicht für jeden Monat überhaupt Umsätze haben. Da wir aber die Umsätze **nach Monat gruppiert** summieren, fehlen die entsprechenden Zeilen (im Beispiel für die Monate April und Juli).

Durch die Verwendung einer "Rahmenabfrage", die alle Monate sicher liefert, lässt sich sicherstellen, dass man immer eine vollständige Jahrestabelle bekommt. Die entsprechenden Umsätze werden dann ebenfalls dazuge`JOIN`t. Wichtig: hier muss ein sog. `LEFT JOIN` verwendet werden, da ja in den beiden Unterabfragen womöglich nicht die identischen Monate vorkommen.

```sql
SELECT  monate.monat,
        umsatz.summe_umsatz
FROM    (SELECT row_num FROM sa_rowgenerator(1, 12)) AS monate(monat)
        LEFT OUTER JOIN
        (
            SELECT  monat,
                    SUM(umsatz) AS summe_umsatz
            FROM    umsatztabelle
            GROUP BY monat
        ) AS umsatz(monat, summe_umsatz)
        ON umsatz.monat = monate.monat
ORDER BY monate.monat
```

| monat | summe_umsatz |
| :---- | -----------: |
| 1     |     3.800,00 |
| 2     |     4.500,00 |
| 3     |     4.250,00 |
| 4     |       (NULL) |
| 5     |     5.100,00 |
| 6     |     4.400,00 |
| 7     |       (NULL) |
| 8     |     4.750,00 |
| ...   |     .... |

Jetzt werden alle Monate des Jahres aufgelistet. An den entsprechenden Monaten ohne Umsatz bleibt die Umsatzspalte leer. Bei der Abfrage über [iSQL](../isql) wird `NULL` angezeigt. Wenn man möchte, kann man die NULL-Umsätze mit der `COALESCE`-Funktion in eine "0" umwandeln.




{{ feedback(page.meta.title, page.meta.section, page.meta.slug) }}
