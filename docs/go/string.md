---
title: Strings in Go
section: go
slug: string
---

# Strings

## Multiline-String

```go
template := `Version: 
Build: 
Datum:`
```


## Uppercase/Lowercase

```go
kleingeschrieben := strings.ToLower(ursprungsString)
grossgeschrieben := strings.ToUpper(ursprungsString)
```


## Substring

```go
beginn := ganzerString[1:5]
```


## Contains

```go
if strings.Contains("einString", "ri") {
}
```


## Stringbuilder

```go
var sb strings.Builder

sb.WriteString("ein String")
sb.WriteString("noch eine Zeile")
sb.WriteString("und noch etwas")

return sb.String()
```


{{ feedback(page.meta.title, page.meta.section, page.meta.slug) }}
