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
SELECT row_num FROM sa_rowgenerator(1, 10, 1);

-- 1, 3, 5, 7, 9
```

Wer nur die geraden Zahlen zwischen 1 und 10 haben will, muss dann den Startwert entsprechend auf 2 setzen:

```sql
SELECT row_num FROM sa_rowgenerator(2, 10, 1);

-- 2, 4, 6, 8, 10
```


## Nutzen

Man möchte die Monatsnummern aller Monate bekommen:

```sql
SELECT row_num FROM sa_rowgenerator(1, 12);
```

Alle Jahre zwischen 1989 und 2022:

```sql
SELECT row_num FROM sa_rowgenerator(1989, 2022);
```


## Verwendung

Im Rahmen einer SQL-Abfrage (View, Prozedur) kann man diese generierte Ergebnistabelle zusammen mit weiteren Daten kombinieren, z.B. summierter Umsatz je Jahr oder Monat.

Wenn man nur den Umsatz nach Monat gruppiert, kann es sein, dass bei Monaten ohne Umsatz diese Zeilen komplett fehlen. Durch die Kombination mit der generierten Liste von Monatsnummern ist sichergestellt, dass für jeden Monat eine Zeile zurückgegeben wird.
