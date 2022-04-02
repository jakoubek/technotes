---
title: Live-Sicherung einer SQL Anywhere-Datenbank
section: sql-anywhere
slug: live-sicherung
tags:
  - TODO
---

# Live-Sicherung einer SQL Anywhere-Datenbank


Die **Live-Sicherung** ist eine *kontinuierliche* Sicherung der Datenbank (genauer: des Transaktionslogs), die *von einem anderen Rechner* ausgeführt wird.

Über das Dienstprogramm **dbbackup** wird eine Client-Verbindung zum Datenbankserver erstellt. Der Datenbankserver sendet dabei die Änderungen des Transaktionslogs kontinuierlich an den Sicherungs-Client.

## Vorgehen

TODO

## Live-Sicherung beenden

Die Live-Sicherung des dbbackup-Programms kann **vom Client nicht beendet** werden. Die Live-Sicherung endet automatisch, wenn der Server heruntergefahren wird.

https://wiki.scn.sap.com/wiki/display/SQLANY/How+to+Create+and+Restore+a+Live+Backup


{{ feedback(page.meta.title, page.meta.section, page.meta.slug) }}
