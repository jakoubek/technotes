---
title: Structs in Go
section: go
slug: struct
---

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


{{ feedback(page.meta.title, page.meta.section, page.meta.slug) }}
