---
title: SQL Anywhere-Datenbank anlegen
section: sql-anywhere
slug: datenbank-anlegen
---

# SQL Anywhere-Datenbank anlegen

Es gibt mehrere Möglichkeiten, eine SQL Anywhere-Datenbank zu erstellen:

- über einen grafischen Assistenten im Datenbank-Browser SQL Central
- auf der Kommandozeile über das Dienstprogramm dbinit
- über eine CREATE DATABASE-Anweisung im iSQL-Tool

## Datenbanken über dbinit erstellen

Hier gehe ich nur auf die Erstellung über das Dienstprogramm `dbinit` ein.

### Dienstprogramm dbinit

Mit Hilfe des Dienstprogrammes `dbinit` kann über eine Kommandozeile ganz schnell eine Datenbank erstellt werden. Der Vorteil dieses Programmes ist, dass sich der Aufruf auch einfach in ein Skript integrieren lässt.

Folgende Angaben sind zwingend oder sinnvollerweise notwendig:

- Name (und ggf. Pfad) der Datenbank
- Name und Passwort des Datenbank-Admin-Benutzers
- Seitengröße
- optional: Name und Pfad des Transaktionslogs
- optional: Name und Pfad des Transaktionslogspiegels

Bei der Eingabe dieses Befehls in einer Kommandozeile (z.B. Eingabeaufforderung unter Windows) empfiehlt es sich, dass gewünschte Zielverzeichnis für die Anlage der Datenbank bereits erzeugt zu haben und in der Eingabeaufforderung dann in dieses Verzeichnis zu wechseln.

```shell
cd C:\Temp\Irgendwohin
mkdir DbDir
cd DbDir
```



Hat man das Verzeichnis mit den SQL Anywhere-Dienstprogrammen nicht über die Pfad-Umgebungsvariable bekannt gemacht, dann muss man das Dienstprogramm über den vollen Pfad aufrufen. Im Fall einer SQL Anywhere 17-Installation wäre das:

```shell
"C:\Program Files\SQL Anywhere 17\Bin64\dbinit.exe"
```

Wichtig sind die Anführungszeichen, da der Pfad Leerzeichen beinhaltet!

Jetzt rufen wir das Dienstprogramm auf und erzeugen die Datenbank:

```shell
"C:\Program Files\SQL Anywhere 17\Bin64\dbinit.exe"
  -dba NameDesDbAdminUsers,ganzSchwierigesPasswort
  -p 4k
  datenbankname.db
```

Im aktuellen Verzeichnis (DbDir) entsteht jetzt die Datenbankdatei *datenbankname.db*. Sie hat eine Seitengröße von 4 kB und der Adminuser heißt *NameDesDbAdminUsers*.

Da wir keine Angaben zum Transaktionslog gemacht haben, wird das Transaktionslog *datenbankname.log* heißen und befindet sich im gleichen Verzeichnis. Es wird vom Datenbankserver beim ersten Start der Datenbank angelegt. Es gibt keinen Transaktionslogspiegel.

Während der Erstellung zeigt das Dienstprogramm eine Reihe von Ausgaben:

```shell
SQL Anywhere-Dienstprogramm Initialisierung Version 17.0.4.2053
CHAR-Kollatierungssequenz:  1252LATIN1(CaseSensitivity=Ignore)
CHAR-Zeichensatzkodierung:  windows-1252
NCHAR-Kollatierungssequenz:  UCA(CaseSensitivity=Ignore;AccentSensitivity=Ignore;PunctuationSensitivity=Primary)
NCHAR-Zeichensatzkodierung:  UTF-8
Datenbank ist nicht verschlüsselt
Systemtabellen werden erstellt
Systemansichten werden erstellt
Optionswerte werden gesetzt
Datenbank "datenbankname.db" erfolgreich erstellt
```

Die Datenbank ist jetzt erzeugt und kann [im nächsten Schritt gestartet](../datenbank-starten) werden.


{{ feedback(page.meta.title, page.meta.section, page.meta.slug) }}
