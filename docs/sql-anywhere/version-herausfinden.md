# SQL Anywhere: Version herausfinden


Manchmal fragt sich der geneigte Admin, welche Version ganz konkret im Einsatz ist.

Mit Hilfe des iSQL lässt sich relativ einfach die Versionsnummer des aktuellen *Datenbankservers* auslesen - diese steht nämlich in der globalen Variable `@@version`:

```sql
SELECT @@version;
```

gibt dann die Versionsnummer zurück, z.B. 16.0.0.2270 oder 17.0.4.2053. Diese Versionen können dann mit den [zuletzt veröffentlichten offiziellen Versionen](https://www.sqla.de/sql-anywhere-aktuelle-versionen/) von SAP verglichen werden.

Daneben ist aber auch interessant, die Version der gestarteten *Datenbank* in Erfahrung zu bringen - diese kann von der des Servers abweichen.

```sql
SELECT operation, version, last_time
FROM SYS.SYSHISTORY
WHERE operation IN ('INIT', 'UPGRADE', 'LAST_START')
```

Diese Abfrage liefert für die aktuelle Datenbank die Information, mit welcher Version die Datenbank ursprünglich erzeugt worden ist (INIT) und mit welcher sie zuletzt gestartet worden ist (das ist die Version des jetzt laufenden und befragten Datenbankservers).
