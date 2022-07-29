---
title: Settings-Tabelle
section: ninox
slug: settings-tabelle
---

## Grundidee

Beim Entwickeln von umfangreicheren Ninox-Datenbanken habe ich immer wieder den Bedarf, Einstellungen *irgendwo* zentral abzulegen und von verschiedenen Stellen aus wieder auszulesen. Dafür eignen sich spezielle Tabellen für "Settings".

Je nach Anwendungsfall kommen zwei verschiedene Formen einer solchen Settings-Tabelle in Frage, eine "flache" Tabelle und eine Art Key-Value-Tabelle.

## A. Flache Tabelle

### A1. Flache Tabelle - ein Konfigurations-Set

In einer flachen Tabelle wird für jeden benötigten Konfigurationswert eine Spalte angelegt. Es gibt nur einen Datensatz in dieser Tabelle.

| CompanyName | AdminEmail |
| :-----------| :--------- |
| Acme Inc.   | admin@example.org |

#### Auslesen eines Wertes

```javascript
ZielTextfeld := first((select FlatSettings).CompanyName)
```

### A2. Flache Tabelle - mehrere Konfigurations-Sets

Womöglich besteht der Bedarf, verschiedene "Konfigurations-Sets" abzubilden.

Dazu erweitert man die Tabelle um eine Spalte für das Set (Abteilung, Filiale, Tochterunternehmen). Beim Zugriff auf ein entsprechendes Setting muss dann zwingend diese "ID" angegeben werden.

| CompanyID | CompanyName | AdminEmail |
| :-------- | :-----------| :--------- |
| 1         | Acme Inc.   | admin@example.org   |
| 2         | Miller Ltd. | admin@millerltd.com |


#### Auslesen eines Wertes

```javascript
ZielTextfeld := first((select FlatSettings where CompanyID = 1).CompanyName)
```

## B. Key-Value-Tabelle

### B1. Key-Value-Tabelle - ein Konfigurations-Set

Zwar lassen sich in Ninox relativ schnell neue Spalten an eine bestehende Tabelle anfügen. Womöglich weiß man jedoch zum Zeitpunkt der Entwicklung noch gar nicht genau, welche Werte abgelegt werden sollen. Oder die Benutzer sollen selbstständig Werte definieren und ablegen können. Für solch ein Szenario eignet sich dann eine Tabellenstruktur, in der Schlüssel-Werte-Paare datensatzweise abgebildet werden:

| Key         | Value             |
| :---------- | :---------------- |
| CompanyName | Acme Inc.         |
| AdminEmail  | admin@example.org |

#### Auslesen eines Wertes

```javascript
ZielTextfeld := first((select KeyValueSettings where Key = "CompanyName").Value)
```

### B2. Key-Value-Tabelle - mehrere Konfigurations-Sets

Auch bei einer Key-Value-Struktur gibt es die Möglichkeit, mehrere Konfigurations-Sets abzubilden. Hierzu wird einfach - wie bei der Variante A2 - auch eine Spalte für die Unterscheidung des Konfigurations-Sets angelegt (hier eben als *CompanyID*):

| CompanyID | Key         | Value               |
| :-------- | :---------- | :------------------ |
| 1         | CompanyName | Acme Inc.           |
| 1         | AdminEmail  | admin@example.org   |
| 2         | CompanyName | Miller Ltd.         |
| 2         | AdminEmail  | admin@millerltd.com |

#### Auslesen eines Wertes

```javascript
ZielTextfeld := first((select KeyValueSettingsMulti where CompanyID = 1 and Key = "CompanyName").Value)
```

## Vor- und Nachteile

Der Vorteil einer flachen Tabelle ist, dass man für jeden Konfigurationswert eine Spalte mit genau dem zum Wert passenden Spaltentyp anlegen kann. Man kann also sicherstellen, dass für einen Zahlen-Konfigurationswert eine Zahlenspalte zur Verfügung steht und somit der Benutzer auch nur Zahlen eingeben kann. Das gleiche für E-Mail-Adressen usw.

Hingegen wird man die Werte in einer Key-Value-Tabelle wohl immer in einer Textspalte hinlegen müssen, weil eine Textspalte alle möglichen Werte aufnehmen kann.


{{ feedback(page.meta.title, page.meta.section, page.meta.slug) }}
