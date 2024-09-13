---
title: Loops in Go
section: go
slug: loops
---

# Loops

## for-Loop

```go
for i := 0; i < 10; i++ {
    sum += i
}
```


## range-Loop

```go
// array of numbers
numbers := [5]int{21, 24, 27, 30, 33}

// use range to iterate over the elements of array
for index, item := range numbers {
  fmt.Printf("numbers[%d] = %d \n", index, item)
}
```


{{ feedback(page.meta.title, page.meta.section, page.meta.slug) }}
