---
title: Bookstack
section: bookstack
slug: index
---


# Bookstack


## Sitemap

Bookstack hat *keine* eingebaute Funktion, um eine XML-Sitemap (die man bei Suchmaschinen einreichen kann) zu erzeugen.
 
Im `api-scripts`-Github-Repository von Bookstack findet sich ein PHP-Skript. Mit diesem kann man eine XML-Sitemap für eine Bookstack-Instanz generieren.

### Vorgehen

- PHP-Skript ins Bookstack-Verzeichnis herunterladen (Adresse s.u.)
- API-Token anlegen
- im Bookstack-Verzeichnis ein Bash-Skript `generate-sitemap.sh` anlegen

```bash
#!/bin/bash

export BS_URL=https://url.der.bookstack.instanz.de
export BS_TOKEN_ID=ApiToken
export BS_TOKEN_SECRET=ApiTokenSecret

# Running the script
php generate-sitemap.php

# Move Sitemap into public dir
mv sitemap.xml public/
```

Im Skript definiert man die URL der Bookstack-Instanz. Diese wird in die Sitemap geschrieben. Zusätzlich hinterlegt man den API-Token und das Secret dazu. Alle drei Werte werden als Umgebungsvariablen gesetzt und vom PHP-Skript ausgelesen.

Da das PHP-Skript die Sitemap-Datei immer im gleichen Verzeichnis erzeugt, verschiebe ich diese am Ende in das `public`-Verzeichnis.

### Informationen

* [Konfiguration von Bookstack](konfiguration)
* [Bookstack-Sitemap-Skript](https://github.com/BookStackApp/api-scripts/tree/main/php-generate-sitemap)

{{ feedback(page.meta.title, page.meta.section, page.meta.slug) }}
