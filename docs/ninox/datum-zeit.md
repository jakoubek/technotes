---
title: Datum und Zeit in Ninox
section: ninox
slug: datum-zeit
---

# Datum und Zeit in Ninox

## Datums- und Zeitfunktionen in Ninox

Ninox stellt für die Arbeit mit Datum und Zeit zumindest die wichtigsten Funktionen zur Verfügung. Mit diesen lassen sich dann mit wenig Aufwand die oft gewünschten Komfortfunktionen selbst umsetzen.

| Funktion | Ergebnis  |
| :------- | :--------- |
| year(Datum)  | Jahreszahl des Datums |
| month(Datum)  | Monatszahl des Datums |
| day(Datum)  | Tageszahl des Datums |
| date(Jahr, Monat, Tag) | Datum "bauen" aus Jahreszahl, Monatszahl, Tageszahl |
| days(Beginn, Ende)  | Anzahl der Tage zwischen zwei Datumswerten |
| age(Datum) | Alter in Jahren, von einem Datum zu "heute" |

## Heutiges Datum

```javascript
let heute := today();
```

### Das aktuelle Jahr

Das aktuelle Jahr lässt sich direkt über die Funktion `year` aus dem heutigen Datum ableiten:

```javascript
let heutigesJahr := year(today());
```

## Alter einer Person in Jahren

Die eingebaute Funktion `age` ermittelt das Alter in Jahren - oder eben die Differenz in Jahren, wenn es sich nicht um ein Geburtsdatum, sondern ein anderes Datum in der Vergangenheit handelt. Wichtig: ist wird immer das *heutige Datum* als Vergleichswert verwendet.

Hinweis: Der jeweilige Tag unterm Jahr wird dabei berücksichtigt. Also: ist heute der 1. August, dann wird bei einem Geburtsdatum, das vor dem 1. August liegt, das aktuelle Jahr mitgezählt. Ist das Geburtsdatum nach dem 1. August, wird das Jahr noch nicht gezählt.

```javascript
let alterInJahren := age(Geburtsdatum);
```


## Jahresanfang und -Ende des aktuellen Jahres

Beim manuellen Zusammenbau eines Datums wird die Funktion `date` verwendet. Dieser übergibt man Jahreszahl, Monatszahl und Tageszahl und bekommt als Ergebnis einen Datumswert.

Jahresanfang und -Ende des jeweils aktuellen Jahres lassen sich rechnerisch recht einfach bestimmen:

- Der Jahresanfang ist immer am 1. Januar, d.h. Tageswert und Monatswert sind 1. Das Jahr müssen wir noch dynamisch bestimmen.
- Das Jahresende ist immer am 31. Dezember, d.h. Tageswert ist 31 und Monatswert 12.

Es bietet sich an, das *heutige Datum* in eine Variable zu schreiben und dann diese an den entsprechenden Stellen wiederzuverwenden. Um den Jahreswert dynamisch zu ermitteln, wird dieser mit der Funktion `year` aus dem heutigen Datum abgeleitet:

```javascript
let heute := today();
let jahresAnfang := date(year(heute), 1, 1);
let jahresEnde := date(year(heute), 12, 31);
```


## Anzahl der Tage im aktuellen Monat

```javascript
let heute := today();
let anzahlTageImAktuellenMonat := days(date(year(heute), month(heute), 1) - 1, date(year(heute), month(heute) + 1, 1) - 1);
```


## die Tagesnummer eines Datums

Um die Nummer eines Datums (z.B. heute) zu ermitteln, kann man sich der Funktion `days` bedienen. Diese liefert die Anzahl der Tage zwischen zwei Datumswerten.

!!! info

    Achtung! Die Funktion `days` rechnet "halb-inklusiv", d.h. sie berechnet die Anzahl von einem Startdatum bis **einschließlich** des Enddatums, jedoch ohne das Startdatum (oder anders herum). Für die Berechnung der Tagesnummer muss man dementsprechend noch einen Tag hinzuzählen. 

Um zu ermitteln, der wievielte Tag des Jahres *heute* ist, rechnen wir wieder die Tage vom *Jahresanfang* bis *heute* und zählen einen Tag dazu:

```javascript
let heute := today();
let tagesNummer := days(date(year(heute), 1, 1), heute) + 1;
```


## Anzahl Tage im Jahr

Die meisten Jahre haben 365 Tage. Für finanzielle Berechnungen o.ä. möchte man aber vielleicht auf Nummer sicher gehen und Schaltjahre erkennen. Wir verwenden die o.g. Möglichkeit zur Bestimmung von Jahresanfang und Jahresende.

```javascript
let heute := today();
let tageImJahr := days(date(year(heute), 1, 1), date(year(heute), 12, 31)) + 1;
```


## Year-to-date

Für die Bestimmung von Year-to-date muss man lediglich die Tagesnummer des heutigen Tages ins Verhältnis zur Gesamtanzahl der Tages des Jahres setzen:

```javascript
let heute := today();
let tagesNummer := days(date(year(heute), 1, 1), heute) + 1;
let tageImJahr := days(date(year(heute), 1, 1), date(year(heute), 12, 31)) + 1;
let ytd := tagesNummer/tageImJahr;
let ytdProzent := ytd * 100;
let ytdProzentGerundet := round(ytdProzent, 2);
```

Die Berechnung liefert einen Dezimalwert, der den bereits abgelaufenen Anteil des Jahres angibt. Möchte man einen Prozentwert anzeigen, muss man dementsprechend mit 100 multiplizieren und ggf. auf z.B. 2 Stellen runden.


{{ feedback(page.meta.title, page.meta.section, page.meta.slug) }}
