# Aktualisierungs-Timestamps in Tabellen

Oft besteht der Bedarf, in einer Tabelle Zeitpunkt der Anlage eines Datensatzes sowie der letzten Änderung identifizieren zu können. Der einfachste Weg ist, in einer Tabelle zwei Timestamp-Spalten anzulegen, eine für den Anlagezeitpunkt und einen für die letzte Änderung.

Über den Default-Wert einer Spalte lässt sich automatisch der Anlagezeitpunkt in den Datensatz schreiben.

Beim Zeitpunkt der letzten Änderung ist das etwas schwieriger – dafür muss man zu einem **Trigger** greifen.

## Tabelle anlegen

```sql
CREATE TABLE table_name (
  id           INTEGER AUTOINCREMENT,
  description  VARCHAR(100) NOT NULL,
  created_at   DATETIME DEFAULT CURRENT TIMESTAMP
  updated_at   DATETIME
);
```

Die Spalte `created_at` wird durch die Angabe eines DEFAULT-Wertes (nur!) beim Anlegen eines Datensatzes auf den jeweiligen jetzigen Zeitpunkt gesetzt. Die Spalte `updated_at` bleibt erst einmal leer.

## Trigger anlegen

```sql
CREATE TRIGGER tub_TABLE_NAME_TS
BEFORE UPDATE ORDER 1
ON table_name
REFERENCING NEW AS newrec
FOR EACH ROW
BEGIN
  SET newrec.updated_at = CURRENT TIMESTAMP;
END;
```

Dieser Trigger wird beim Ändern eines Datensatzes *gefeuert* (genauer: vor dem Festschreiben der Änderung) und setzt die Spalte `updated_at` auf den jetzigen Zeitpunkt.
