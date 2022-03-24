# Archivsicherung einer SQL Anywhere-Datenbank

Eine Archivsicherung sichert die komplette Datenbank in eine oder mehrere – abhängig von der Größe der Datenbank – Dateien, die alle erforderlichen Sicherungs- und Wiederherstellungsinformationen enthalten.

**Wichtig**: alle angegebenen Pfade gelten aus Sicht des Datenbank-Servers, **nicht** des Clients!

## Archivsicherung per iSQL

```sql
BACKUP DATABASE TO 'D:\\TEMP\\SQLA\\Archivsicherung\\database_backup'
```

Die Sicherung erfolgt ins Verzeichnis **D:\TEMP\SQLA\Archivsicherung**. Dabei ist **database_backup** der Basisname der Sicherungsdateien. Die erste Datei heißt **database_backup.1**. Abhängig von der Größe der gesicherten Datenbank entstehen weitere Dateien mit den Dateiendungen “.2”, “.3”, “.4”, usw.

## Wiederherstellen aus einer Archivsicherung

Die Wiederherstellung einer Datenbank aus einer Archivsicherung kann entweder über iSQL erfolgen oder über den Wiederherstellungs-Assistenten in SQL Central (früher: "Sybase Central").

## Wiederherstellen über iSQL

```sql
RESTORE DATABASE 'D:\\NeueDatenbank\\datenbankdatei.db'
FROM 'D:\\TEMP\\SQLA\\Archivsicherung';
```

Beim Wiederherstellen gibt man den Pfad zu der **neuen** Datenbankdatei an (die erzeugt werden soll). Als Quelle für die Wiederherstellung wird jetzt (im Unterschied zum Sichern) nur noch der Name des Sicherungsverzeichnisses angegeben.

