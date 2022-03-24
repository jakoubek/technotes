# SQL Anywhere: Transaktionslog


## Dienstprogramm dblog

Es gibt ein Dienstprogramm `dblog.exe`, mit dem man über die Kommandozeile das Transaktionslog einer Datenbank verwalten kann.


## Transaktionslog-Spiegel

Die Transaktionslog-Spiegeldatei

- ist eine identische Kopie des Transaktionslogs
- wird vom Datenbankserver zeitgleich mit dem Transaktionslog geschrieben

### Vorteile

bietet vollständige Wiederherstellung bei Beschädigung des Transaktionslogs

### Nachteile

(minimal) erhöhte Belastung des DB-Servers durch doppelten Schreibvorgang

### Best Practices

- sollte (= "muss") auf dem gleichen Rechner liegen
- weil: der Datenbankserver **stoppt**, wenn Verbindung zwischen den Rechnern abbricht
- sollte auf einer separaten Partition untergebracht werden (Performance)

## Infos

http://sqlanywhere.blogspot.com/2018/08/controlling-sql-anywhere-transaction.html

