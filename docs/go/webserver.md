---
title: Webserver in Go
section: go
slug: webserver
---

# Webserver in Go


## Minimaler Webserver

```go
package main

import (
  "log"
  "net/http"
)

func main() {
  http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
    w.Write([]byte("Hallo Welt!"))
  })

  log.Fatal(http.ListenAndServe(":8080", nil))
}
```


{{ feedback(page.meta.title, page.meta.section, page.meta.slug) }}
