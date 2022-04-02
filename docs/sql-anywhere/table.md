---
title: "SQL Anywhere: Arbeit mit Tabellen"
section: sql-anywhere
slug: table
---

# SQL Anywhere: Arbeit mit Tabellen






## Tabelle umbenennen

```sql
ALTER TABLE alter_tabellenname RENAME neuer_tabellenname;
```


## Tabelle löschen

!!! warning "Warnung"

    Achtung! Die Tabelle samt Inhalt wird sofort gelöscht und kann danach auch nicht wiederhergestellt werden (Ausnahme: aus einem Backup natürlich schon).

```sql
DROP TABLE tabellenname;
```


## Defaultwert einer Tabellenspalte ändern

```sql
ALTER TABLE tabellenname MODIFY spalte1 DEFAULT 1;
```


{{ feedback(page.meta.title, page.meta.section, page.meta.slug) }}
