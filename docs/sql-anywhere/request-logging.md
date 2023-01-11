---
title: Request Logging
section: sql-anywhere
slug: request-logging
---

# Request Logging

Mittels *Request Logging* lässt sich untersuchen, welche SQL-Statements oder Prozeduraufrufe ein Clientprogramm an eine SQL Anywhere-Datenbank sendet.


## aktueller Stand prüfen

```sql
SELECT PROPERTY('RequestLogging');
SELECT PROPERTY('RequestLogFile');
```


Mögliche Werte sind SQL, PLAN, HOSTVARS, PROCEDURES, TRIGGERS, OTHER, BLOCKS, REPLACE, ALL und NONE.

NONE = keine Protokollierung


## Request Logging einschalten

```sql
-- RL einschalten für die genannten Elemente
CALL sa_server_option('RequestLogging', 'SQL+PROCEDURES+BLOCKS');

-- nur Statements für diese Verbindungsnummer protokollieren
CALL sa_server_option('RequestFilterConn', '8' );

-- Statements in diese Datei protokollieren
CALL sa_server_option('RequestLogFile', 'D:\Database\requests.log');
```


## schnell einschalten

```sql
CALL sa_server_option('RequestLogging', 'SQL+PROCEDURES+BLOCKS');
CALL sa_server_option('RequestLogFile', 'D:\Database\requests.log');
```

## ausschalten

Request Logging lässt sich ausschalten, indem man die Serveroption *RequestLogging* auf `NONE` setzt.

```sql
CALL sa_server_option('RequestLogging', 'NONE');
```

## notwendige Privilegien

Der Datenbank-Benutzer muss das Systemprivileg `MANAGE PROFILING` besitzen, um die für Request Logging relevanten Serveroptionen setzen zu können.

{{ feedback(page.meta.title, page.meta.section, page.meta.slug) }}
