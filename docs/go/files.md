---
title: Dateien und Verzeichnissein Go
section: go
slug: files
---

# Dateien und Verzeichnisse


## Prüfen, ob ein Verzeichnis existiert

```go
_info_, err := os.Stat(directoryname)
if os.IsNotExist(err) {
    // dir does not exist
}
```


## Prüfen, ob eine Datei existiert

```go
info, err := os.Stat(filename)
if os.IsNotExist(err) {
    return false
}
return !info.IsDir()
```


## Datei einlesen

```go
fileContent, err := os.ReadFile(templateFile)  
if err != nil {  
    log.Fatal(err)  
}
```


## Datei schreiben

```go
f, err := os.Create("test.txt")
    if err != nil {
        fmt.Println(err)
        return
    }
    l, err := f.WriteString("Hello World")
    if err != nil {
        fmt.Println(err)
        f.Close()
        return
    }
    fmt.Println(l, "bytes written successfully")
    err = f.Close()
    if err != nil {
        fmt.Println(err)
        return
    }
```


{{ feedback(page.meta.title, page.meta.section, page.meta.slug) }}
