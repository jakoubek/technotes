---
title: Inkrementelle Sicherung einer SQL Anywhere-Datenbank
section: sql-anywhere
slug: inkrementelle-sicherung
---

# Inkrementelle Sicherung einer SQL Anywhere-Datenbank

## Inkrementelle Sicherung

```sql
BACKUP DATABASE
  DIRECTORY 'Pfad\\zum\\Backupverzeichnis'
  TRANSACTION LOG ONLY
  TRANSACTION LOG TRUNCATE;
```

Inkrementelle Sicherung

```shell
"%SQLANY11%\bin32\dbbackup.exe"
  -c "ENG=ddd11;DBN=ddd11;UID=dba;PWD=sql"
  -o bkup\dbbackup_log.txt
  -n
  -t
  -x
  bkup\generation10\logs
```

### Parameter

* o Ausgabemeldungen in Datei umleiten
* n Namenskonvention in den gespeicherten Transaktionslogs ändern
* t **Erstellt eine Sicherung, die als inkrementelle Sicherung verwendet werden kann, da das Transaktionslog auf die letzte gesicherte Kopie der Datenbankdatei(en) angewendet werden kann.**
* x Sichert das vorhandene Transaktionslog, das ursprüngliche Transaktionslog wird gelöscht und ein neues wird gestartet. Verwenden Sie diese Option nicht, wenn Sie mit einer Datenbankspiegelung arbeiten.

[https://sqlanywhere-forum.sap.com/questions/4760/restoring-incrementallive-backup-failure](https://sqlanywhere-forum.sap.com/questions/4760/restoring-incrementallive-backup-failure)


{{ feedback(page.meta.title, page.meta.section, page.meta.slug) }}
