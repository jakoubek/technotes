---
title: Ein minimales Backup-Konzept für eine SQL Anywhere-Datenbank
section: sql-anywhere
slug: minimales-backup
---

## Hintergrund

Für eine Datenbank, die in einem Unternehmen wirklich produktiv genutzt wird, muss es ein Backup-Konzept geben. Ein einfaches [Backup per Dateikopie] ist für eine dauerhaft laufende Datenbank aber nicht möglich.

## Was sichert man?

Eine Datenbank besteht aus zwei Bestandteilen: den Dateien für den eigentlichen Datenbestand und dem Transaktionslog, in das fortlaufend die Änderungen am Datenbestand protokolliert werden.

!!! warning "Achtung"

    Das Kopieren von Dateien funktioniert im Regelfall nur dann sauber, wenn diese Dateien nicht genutzt, d.h. nicht von einem anderen Programm geöffnet sind.  
    Läuft eine Datenbank, dann sind die dazugehörigen Datenbank-Dateien vom Datenbank-Server (der Software) geöffnet und können nicht kopiert werden. 

Weil der Datenbank-Server die Dateien der laufenden Datenbank geöffnet hat, können diese **von außen** nicht einfach weggesichert (kopiert) werden.

Der Datenbank-Server selbst hingegen kann das machen - er hat die Dateien ja bereits im Zugriff.

### Vollbackup

Sichert man die komplette Datenbank, spricht man von einem sog. *Vollbackup*. Dies verursacht - abhängig vom Umfang der Datenbank - entsprechende Last auf dem Server. Deshalb wird man versuchen, das Vollbackup zeitlich in die Nacht bzw. in Phasen der geringen Datenbank-Nutzung zu verlegen.

Das Ergebnis eines Vollbackups ist eine Kopie aller Datenbank-Dateien an einem anderen Ort (Partition, Netzlaufwerk). Diese Kopien befinden sich **nicht im Zugriff** des Datenbank-Servers (sind also nicht geöffnet) und können deshalb von dort weggesichert werden.

### Backup des Transaktionslogs

Schneller lässt sich das Transaktionslog sichern. Dieses ist im Regelfall kleiner als die eigentliche Datenbank (zumindest wenn es regelmäßig bereinigt worden ist). Im Transaktionslog sind jedoch nur die *Änderungen am Datenbestand* protokolliert.

## Backup-Konzept

Man führt regelmäßig (z.B. jede Nacht) ein **Vollbackup** durch. Dadurch hat man den kompletten Datenbestand zum Sicherungszeitpunkt in *nicht geöffneten Dateien*.

Allerdings ist der Datenstand des Vollbackups zum Zeitpunkt, wenn man ggf. am Folgetag aus dem Backup die Datenbank wiederherstellen möchte, bereits veraltet: alle Änderungen, die seit dem Vollbackup erfolgt sind, sind dort noch nicht zu finden.

In einem zweiten Schritt möchte man deshalb die Zeiten *zwischen den Vollbackups* verkürzen. Dazu kann die Datenbank automatisch und regelmäßig das **Transaktionslog wegsichern**. Hier bieten sich stündliche oder sogar viertelstündliche Intervalle an.

Bei der **Wiederherstellung** eines solcherart gesicherten Datenbank müssen dann zuerst die weggesicherten Datenbank-Dateien des Vollbackups an den Zielpfad kopiert werden. Anschließend werden alle gesicherten Transaktionslogs *seit dem Vollbackup* nacheinander auf die wiederhergestellte Datenbank angewendet. Als Resultat erhält man den Datenstand zum Zeitpunkt der letzten Sicherung des Transaktionslogs vor dem evtl. Crash.

Bei einer täglichen Vollsicherung und einer viertelstündlichen Sicherung des Transaktionslogs "schrumpfen" damit die maximal verlorengehenden Daten auf die Änderungen der letzten Viertelstunde vor dem Crash.

## Detailbeschreibungen

* [Vollbackup](../vollbackup/)
* [Backup des Transaktionslogs](../backup-transaktionslog/)
* [Wiederherstellung aus einem Backup](../backup-wiederherstellen/)


{{ feedback(page.meta.title, page.meta.section, page.meta.slug) }}



