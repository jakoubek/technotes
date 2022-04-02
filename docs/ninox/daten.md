---
title: "Ninox: Arbeiten mit Datensätzen"
section: ninox
slug: daten
---

# Ninox: Arbeiten mit Datensätzen

## Datensatz kopieren

Kopiert den aktuellen Datensatz (`this`) in eine Variable `myNew`.

```javascript
let myNew := duplicate(this);
```

## Tabelle leeren

```javascript
delete select Tabellenname;
```

## Link zum Datensatz

```javascript
urlOf(this)
```

## Loop über Datenbank-Abfrage

```javascript
for record in select Tabellenname where spalte = 1 do

end;
```

## Datensatz programmatisch anlegen

```javascript
let ds := (create Tabellenname);
ds.(Name := namensVariable);
ds.(PLZ := plzVariable);
ds.('Angelegt am' := now());
```


{{ feedback(page.meta.title, page.meta.section, page.meta.slug) }}
