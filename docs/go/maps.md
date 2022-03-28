# Maps in Go


## Eine Map definieren

Beispiel für eine Map, bei der der Schlüssel und der Wert Strings sind:

```go
var myMap map[string]string
```

Beispiel für eine Map, bei der der Schlüssel ein String und der Wert ein Integer sind:

```go
var myMap map[string]int
```


## Prüfen, ob eine Map einen Schlüssel beinhaltet

```go
data := map[string]int{
    "a": 1,
    "b": 2,
    "c": 3,
}

val, ok := data["a"]
fmt.Println(val, ok)
val, ok = data["d"]
fmt.Println(val, ok)
```

Ausgabe:
```
1 true
0 false
```
