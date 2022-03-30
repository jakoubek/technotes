---
tags:
  - TODO
---

# Datum und Zeit in Ninox

## Anzahl der Tage im aktuellen Monat

```javascript
let heute := today();
let anzahlTageImAktuellenMonat := days(date(year(heute), month(heute), 1) - 1, date(year(heute), month(heute) + 1, 1) - 1);
```
