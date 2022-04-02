---
title: Request Logging
section: sql-anywhere
slug: request-logging
---

# Request Logging


## aktueller Stand prüfen

```sql
SELECT PROPERTY('RequestLogging');
SELECT PROPERTY('RequestLogFile');
```


Mögliche Werte sind SQL, PLAN, HOSTVARS, PROCEDURES, TRIGGERS, OTHER, BLOCKS, REPLACE, ALL und NONE.

NONE = keine Protokollierung


## Request Logging einschalten

```sql
CALL sa_server_option('RequestLogging', 'SQL');
CALL sa_server_option('RequestLogging', 'SQL+PROCEDURES+BLOCKS');

CALL sa_server_option('RequestFilterConn', '8' );

CALL sa_server_option('RequestLogFile', 'D:\ZSP-Datenbank\Protokolle\requests.log');
```


## schnell einschalten

```sql
CALL sa_server_option('RequestLogging', 'SQL+PROCEDURES+BLOCKS');
CALL sa_server_option('RequestLogFile', 'D:\ZSP-Datenbank\Protokolle\requests.log');
```

## ausschalten

```sql
CALL sa_server_option('RequestLogging', 'NONE');
```


{{ feedback(page.meta.title, page.meta.section, page.meta.slug) }}
