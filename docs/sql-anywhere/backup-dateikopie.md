---
title: Backup einer SQL Anywhere-Datenbank durch Dateikopie
section: sql-anywhere
slug: backup-dateikopie
---

## Hintergrund

SQL Anywhere ist eine sog. *Self-contained database*. Das bedeutet, dass sich die Daten **einer** Datenbank in mindestens **einer Datei** befinden (bzw. zwei Dateien, mit [Transaktionslog](../transaktionslog/)) und nicht &mdash; wie bei anderen Datenbanken &mdash; in einer von der Datenbank-Software verwalteten Verzeichnisstruktur.

## Backup durch Dateikopie

Eine SQL Anywhere-Datenbank lässt sich deshalb am einfachsten dadurch sichern, dass man die zur Datenbank gehörigen Dateien einfach (weg)kopiert.

!!! warning "Achtung"

    Das Kopieren von Dateien funktioniert im Regelfall nur dann sauber, wenn diese Dateien nicht genutzt, d.h. nicht von einem anderen Programm geöffnet sind.  
    Läuft eine Datenbank, dann sind die dazugehörigen Datenbank-Dateien vom Datenbank-Server (der Software) geöffnet und können nicht kopiert werden.

Da man dazu den Datenbank-Server (die Software, nicht den Rechner oder Host) herunterfahren muss, ist die Sicherung durch Dateikopie kein taugliches Konzept für die Sicherung einer produktiv genutzten Datenbank.

Hier stelle ich ein [minimales Backup-Konzept](../minimales-backup/) für eine dauerhaft laufende Datenbank vor.

{{ feedback(page.meta.title, page.meta.section, page.meta.slug) }}

