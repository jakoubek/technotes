---
title: SQL Anywhere-Datenbank starten
section: sql-anywhere
slug: datenbank-starten
---

# SQL Anywhere-Datenbank starten

Die [im ersten Schritt](../datenbank-anlegen) angelegte Datenbank existiert jetzt, aber der Server hat sie nicht gestartet.

Über die gleiche Kommandozeile kann man diese Datenbank jetzt einfach mal testweise starten. Ich verwende dazu das Programm `dbeng17.exe` - den sog. *Personal Server*. Das ist ein Datenbankserver, der nur zum lokalen Test (z.B. für Entwickler) gedacht ist.

Diesem Programm übergibt man einfach den Namen der zu startenden Datenbank:

```shell
"C:\Program Files\SQL Anywhere 17\Bin64\dbeng17.exe" datenbankname.db
```

Rechts unten im Tray (unter Windows) sieht man dann ein kleines Blitz-Symbol. Über das Kontextmenü lässt sich *Wiederherstellen* aufrufen. Dann öffnet sich ein Datenbankfenster, das die jeweils aktuellen Ausgaben des Servers anzeigt.

Die Datenbank ist also vom Server gestartet worden. Im Verzeichnis ist jetzt eine weitere Datei enstanden, *datenbankname.log*. Das ist das Transaktionslog.

Über *Herunterfahren* (im Datenbankfenster) kann jetzt die Datenbank wieder gestoppt werden.


{{ feedback(page.meta.title, page.meta.section, page.meta.slug) }}
