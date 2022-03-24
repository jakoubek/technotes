# Clientseitige Sicherung einer SQL Anywhere-Datenbank


Die clientseitige Sicherung erfolgt mit Hilfe des Dienstprogrammes `dbbackup`.

```shell
dbbackup.exe -c "UID=...;PWD=...;SERVER=...." D:\\\\Backup
```

Das `dbbackup`-Dienstprogramm baut eine Client-Verbindung zum Datenbankserver auf und sichert die laufende Datenbankdatei sowie das Transaktionslog in ein Verzeichnis **relativ zum Client**.

## Serverseitige Sicherung mit dbbackup

Mit der Option `-s` wird der Server veranlasst, eine **serverseitige** Sicherung (`BACKUP DATABASE`) durchzuführen.
