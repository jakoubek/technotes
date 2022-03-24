# Verschiedene SQL-Funktionen


## Printf

Printf-Funktionen gibt es in vielen Programmiersprachen. Sie dienen dazu, in einem Text an einer oder mehreren Stellen Platzhalter durch variable Inhalte zu ersetzen.

Auch in einer SQL Anywhere-Prozedur kann man diese Funktionalität nutzen. Es gibt dazu eine Systemprozedur `xp_sprintf`.

Wichtig dabei ist, dass diese mit der Zielvariable als ersten Parameter aufgerufen wird. Es handelt sich also **nicht** um eine Funktion, die einen Wert liefert, den man der Zielvariable zuweisen kann.

```sql
DECLARE ls_anrede VARCHAR(100);
DECLARE ls_vorname VARCHAR(50);
DECLARE ls_nachname VARCHAR(50);

SET ls_vorname = 'James';
SET ls_nachname = 'Bond';

CALL xp_sprintf(ls_anrede, 'Hallo %s %s', ls_vorname, ls_nachname);
```

Dieses Snippet hätte als Ergebnis in der Variable `ls_anrede` den Wert **Hallo James Bond**.



## One row only

Im Laufe der Zeit sammeln sich in einer Datenbank-Anwendung immer auch Utility-Funktionen und -Tabellen an. Eine davon, die ich immer wieder hilfreich finde: **eine Tabelle, die genau einen Datensatz beinhaltet**. Dabei muss sichergestellt werden, dass Nutzer diesen nicht löschen können und auch keine weiteren Datensätze anlegen können.

```sql
CREATE TABLE one_row_only (
    one_row_only INTEGER NOT NULL DEFAULT 1 CHECK ( one_row_only = 1 ) PRIMARY KEY,
    started_at TIMESTAMP NOT NULL
);

CREATE TRIGGER tdb_one_row_only BEFORE DELETE ON one_row_only
FOR EACH ROW
BEGIN
    ROLLBACK TRIGGER WITH RAISERROR 99999 'Do not attempt to delete from one_row_only';
END;

INSERT INTO one_row_only VALUES ( DEFAULT, CURRENT TIMESTAMP );
COMMIT;
```

### Hintergrund

Nur ein Datensatz ....

Die Primärschlüssel-Spalte `one_row_only` ist vom Typ `INTEGER`, hat als Standardwert den Wert 1 und die CHECK-Clause stellt sicher, dass als Inhalt nur der Wert 1 akzeptiert wird. Weil auf einer Primärschlüssel-Spalte automatisch ein UNIQUE-Index liegt, kann in dieser Tabelle nur ein Datensatz angelegt werden.

.... der nicht gelöscht werden kann:

Zusätzlich liegt auf der Tabelle ein `BEFORE DELETE`-Trigger, der einen Fehler wirft und die angestrebte Änderung rückgängig macht.
