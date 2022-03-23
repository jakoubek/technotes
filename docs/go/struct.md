# Structs


## Anonymous structs

```go
variableName := struct{
    code string
    name string
}{
    "01", "John"
}
```

### Array of anonymous structs

```go
variableName := []struct{
    code string
    name string
}{
    {"01", "John"},
    {"02", "Mary"},
}
```

