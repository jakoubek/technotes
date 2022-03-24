# SQL Anywhere-Datenbank entladen


## Dienstprogramm dbunload

```shell
dbunload
    -c "UID=dba;PWD=sql;SERVER=YourServerName"
    -r ReloadFile.sql
    Unloaddirectory
```

**Achtung: der Entlade-Pfad wird immer serverseitig interpretiert!**

## LOAD vs INPUT

-ii Verwendet die UNLOAD-Anweisung, um Daten aus der Datenbank zu extrahieren, und die LOAD-Anweisung in der Datei reload.sql, um die Datenbank wieder mit Daten zu füllen. Dies ist die Standardeinstellung.

-ix Verwendet die UNLOAD-Anweisung, um Daten aus der Datenbank zu extrahieren, und die INPUT-Anweisung von Interactive SQL in der Datei reload.sql, um die Datenbank wieder mit Daten zu füllen.
