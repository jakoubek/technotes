---
title: System-Views und -Prozeduren
section: sql-anywhere
slug: system
---

# System-Views und -Prozeduren


## Prozeduren/Funktionen abfragen

Es besteht die Möglichkeit, über `sysprocedure` den Katalog an Stored Procedures (bzw. Funktionen) abzufragen.

Evtl. weiß man, dass sich in der Datenbank eine Prozedur befindet, die irgendwie mit der Tabelle *kundentabelle* zu tun hat. Allerdings kennt man den Namen der Prozedur nicht. So kann man per iSQL den Katalog abfragen und bekommt eine Liste mit allen Prozeduren, die diese Tabelle verwenden (genauer: bei denen der Tabellenname als String erscheint - es kann sich natürlich auch um einen Kommentar im SQL-Quelltext handeln).

```sql
SELECT *
FROM   sysprocedure
WHERE  proc_defn LIKE '%kundentabelle%';
```


{{ feedback(page.meta.title, page.meta.section, page.meta.slug) }}
