# Datum und Zeit

## Datumsformat

```go
2006-01-02 15:04:05
```


## Datumsobjekt erzeugen

```go
myDate := time.Now()
```


## Aktuelles Jahr

```go
currentYear := time.Now().Format("2006")
```


## Zeitdauer messen

```go
start := time.Now()
...
end := time.Now()
elapsed := time.Since(start)
```
