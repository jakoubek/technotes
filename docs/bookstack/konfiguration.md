---
title: Bookstack-Konfiguration
section: bookstack
slug: konfiguration
---

# Bookstack-Konfiguration

Folgende Werte trage ich immer noch in der Enviroment-Datei (.env) nach:

## Zeitzone

```php
APP_TIMEZONE=Europe/Berlin
```


## Sitzungsdauer

Das bezieht sich darauf, wie lange man als angemeldeter Benutzer angemeldet bleibt. Nach Ablauf dieser Zeit muss man sich wieder erneut anmelden. Ich habe diesen Wert auf 43.200 (Minuten) gesetzt, also 30 Tage.

```php
SESSION_LIFETIME=43200
```



{{ feedback(page.meta.title, page.meta.section, page.meta.slug) }}

