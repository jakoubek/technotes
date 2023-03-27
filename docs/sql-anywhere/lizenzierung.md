---
title: Lizenzierung
section: sql-anywhere
slug: lizenzierung
---

# SQL Anywhere lizenzieren

Über das Kommandozeilen-Programm `dblic` (*Server Licensing utility*) lassen sich Lizenzdaten hinterlegen.

Das Programm hinterlegt die Lizenzdaten dazu in einer speziellen Datei, die den gleichen Namen wie die Server-Executable trägt, jedoch mit der Endung `.lic`.

## Syntax für den Aufruf

Die offizielle Syntax für den Aufruf lautet laut Handbuch so:

```
dblic [ options ] license-file [ "user-name" "company-name" ]
```

Folgende Optionen sind möglich:

| Option  | Bedeutung  | Erklärung |
| ------- | ---------- | --------- |
| -l type | Lizenztyp  | mögliche Werte: "perseat" oder "processor" |
| -u license-number | Anzahl an lizenzierten Benutzern bzw. Prozessoren ||
| -o filename  | Ausgabe in Datei umleiten | |
| -q           | *Quiet mode* - keine Ausgaben auf der Konsole | |
| license-file | Pfad zur .lic- oder .exe-Datei | |

Benutzername und Firmenname sind optional. Ich verwende für beide immer die gleichen Angaben, i.d.R. die Abkürzung des Firmennamens meines Kunden.

Die Zieldatei (im Handbuch *license-file* genannt) kann wahlweise die Server-Executable sein **oder** die gleichnamige `.lic`-Datei. Die Lizenzdaten werden immer in der `.lic`-Datei hinterlegt. Das `dblic`-Programm findet diese Lizenzdatei auch, wenn man als Pfad die Server-Executable angibt.

## Beispiel

Hier ein beispielhafte Lizenzierung von 10 Benutzerlizenzen (*concurrent user*, also "perseat"). Die SQL Anywhere-Installation befindet sich auf einem Windows-Server. Die Ausgaben in der Konsole sollen in eine Datei geschrieben werden. Es wird die 64-Bit-Variante von SQL Anywhere lizenziert.

```
dblic.exe -l perseat -u 10 -o lizenzierung.log
    "C:\Program Files\SQL Anywhere 16\Bin64\dbsrv16.exe" "Acme" "Acme"
```



{{ feedback(page.meta.title, page.meta.section, page.meta.slug) }}

