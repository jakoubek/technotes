---
title: Structs in Go
section: go
slug: struct
---

# Structs


## Anonymous structs

Ein anonymer Struct ist ein Struct, der ^^nicht^^ zuerst als Typ definiert und dann einer neuen Variable zugewiesen wird. Statt dessen werden Definition und Variableninstanziierung inkl. Wertzuweisung in einem Schritt gemacht.

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


{{ feedback(page.meta.title, page.meta.section, page.meta.slug) }}
