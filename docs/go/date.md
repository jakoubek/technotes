---
title: Datum und Zeit in Go
section: go
slug: date
---

# Datum und Zeit in Go

## Datumsformat

Go verwendet ein recht eigensinniges Datumsformat. Anstatt Zeichen wie *Y*, *M*, *D* usw. zu verwenden, gibt es ein Referenzdatum. Die einzelnen Werte des Referenzdatums - die sich vom Wert nicht überschneiden - können zur Festlegung des gewünschten Datums verwendet werden.

### Das Referenzdatum in Go

```go
2006-01-02 15:04:05
```

- Jahr: 2006
- Monat: 01
- Tag: 02
- Stunde: 15
- Minute: 04
- Sekunde: 05
- Monatsname: January bzw. Jan
- Wochentag: Monday bzw. Mon

Das bedeutet: möchte man ein Datum im *alten* deutschen Format ausgeben, verwendet man (anstatt DD.MM.YYYY) "02.01.2006". Dieses Beispiel gibt das heutige Datum aus:

```go
time.Now().Format("02.01.2006") // 24.03.2023
```


## Datumsobjekt erzeugen

```go
myDate := time.Now()
```


## Aktuelles Jahr

```go
currentYear := time.Now().Format("2006")
```


## ISO-Format

```go
fmt.Println(time.Now().Format("2006-01-02"))
```


## Zeitdauer messen

```go
start := time.Now()
...
elapsed := time.Since(start)
fmt.Println("execution time:", elapsed)
```


## Datum parsen

```go
package main

import (
  "fmt"
  "log"
  "time"
)

// Datumsformat
const MY_DATE_FORMAT = "2006-01-02"

func main() {
  mein_datums_string := "2022-03-28"
  t, err := time.Parse(MY_DATE_FORMAT, mein_datums_string)
  if err != nil {
    // Ausgabe, wenn der String NICHT mit dem
    // erwarteten Datumsformat geparst werden konnte
    log.Fatal(err)
  }
  // Ausgabe des erfolgreich geparsten Datums
  fmt.Println(t)
}
```


{{ feedback(page.meta.title, page.meta.section, page.meta.slug) }}
