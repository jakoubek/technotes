---
title: REI3
section: rei3
slug: index
tags:
  - Low Code
---

# REI3, die offene Low-Code-Plattform

**REI3**  ist eine webbasierte Plattform, die es ermöglicht, datenbankgestützte Softwarelösungen ohne herkömmliche Programmierkenntnisse zu entwickeln und zu implementieren. REI3 ist Open-Source und kostenfrei nutzbar.

## Technik

REI3 ist ein in [Go](/go/) geschriebener Webserver, der eine [PostgreSQL-Datenbank](/postgresql/) verwendet. Es kann unter Linux und Windows sowohl als Anwendung wie auch als Dienst betrieben werden.

## Entwicklung einer Anwendung

Die Entwicklung einer Anwendung erfolgt ebenfalls über das Webfrontend, im sogenannten *Builder*-Modus.
Für den einfachen Einstieg genügt es, die Datenbank-Struktur einer Anwendung über eine grafische Maske zu erzeugen. Dabei werden im Hintergrund die notwendigen Tabellen in der Datenbank angelegt. Für diese Tabellen (*Relationen* genannt) können dann Formulare erzeugt werden. Auch das erfolgt im grafischen Modus ohne "Programmierung".

Erst wenn man bei der Arbeit mit den Daten ausgefeiltere Anforderungen hat, muss man Programm-Code erzeugen. Daten-orientierte Bearbeitungen werden im Backend entwickelt. Dabei handelt es um Trigger und Stored Procedures. Diese werden in [PL/pgSQL](https://de.wikipedia.org/wiki/PL/pgSQL){target="_blank"} geschrieben. Frontend-Funktionen - die auf Ereignisse in Formularen reagieren - können in JavaScript geschrieben werden.

## Updates

Steht eine neue Version der zugrundeliegenden REI3-Plattform zur Verfügung, genügt es, den Dienst zu stoppen und das ausführbare Programm auszutauschen und dann neu zu starten. Evtl. notwendige Anpassungen an der Datenbank-Struktur werden dann automatisch vorgenommen.


## Informationen

* [REI3-Website](https://rei3.de/)
* [REI3-Forum](https://community.rei3.de/)
* [REI3-Builder-Dokumentation](https://rei3.de/de/docs/builder)

{{ feedback(page.meta.title, page.meta.section, page.meta.slug) }}
