---
title: MkDocs
section: misc
slug: mkdocs
---

# MkDocs

MkDocs ist eine in Python geschriebenes Programm, mit dem man aus Textdateien eine Website generieren lassen kann. MkDocs wird häufig genutzt, um Online-Dokumentationen zu erstellen. [Diese Website hier](/info/) wird ebenfalls mit MkDocs erzeugt.


## Installation

MkDocs benötigt Python und `pip`, das Standard-Paketinstallationstool von Python.

```shell
pip install mkdocs
```


## Grundsätzliches Vorgehen



```shell
mkdocs new testprojekt
cd testprojekt
mkdocs serve
```

- mit `mkdocs new projektname` wird ein neues Projekt angelegt - es entsteht ein neues Verzeichnis *testprojekt*
- man wechselt in das Verzeichnis
- mit dem Kommando `mkdocs serve` wird ein lokaler Webserver gestartet (auf [http://localhost:8000](http://localhost:8000))
- über diesen kann man in einem Browserfenster jeweils aktuell den Inhalt der eigenen Dokumentationswebsite sehen - MkDocs aktualisiert bei jedem Speichern einer Datei sofort die Website

### Website generieren

Möchte man zu einem gewissen Datenstand aus den Textdateien eine Web-Version erzeugen, kann man das mit dem Kommando `mkdocs build` machen. Dann wird ein Unterzeichnis `site` angelegt und in diesem die statischen HTML-Dateien erzeugt. Diese kann man dann auf einem Webserver ablegen.


## Zusätzliche Pakete

Zusätzlich installiere ich in allen meinen MkDocs-Projekten immer noch die folgenden beiden Pakete:

- [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) ist ein modernens und mächtiges Theme mit vielen eingebauten Funktionen, das sich sehr gut für Dokumentations-Websites eignet
- [mkdocs-macros](https://mkdocs-macros-plugin.readthedocs.io/en/latest/) ist ein Plugin, das Variablen, Makros und Scripting innerhalb von MkDocs bereitstellt

### Installation

```shell
pip install mkdocs-material
pip install mkdocs-macros-plugin
```


## Informationen

- [MkDocs-Website](https://www.mkdocs.org/)
- [Material for MkDocs-Theme](https://squidfunk.github.io/mkdocs-material/)
- [mkdocs-macros](https://mkdocs-macros-plugin.readthedocs.io/en/latest/)



{{ feedback(page.meta.title, page.meta.section, page.meta.slug) }}

