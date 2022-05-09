---
title: Arrays in Xojo
section: xojo
slug: arrays
---

# Arrays in Xojo


## Array anlegen

```vbnet
Var arr() As String
```


## Elemente hinzufügen

```vbnet
arr.AddRow("Eins")
arr.AddRow("Zwei")
arr.AddRow(StringVariable)
```

## Element aus Array entfernen

TODO


## Anzahl der Elemente im Array zählen

```vbnet
Var anzahl As Integer = arr.Ubound() + 1
```


## Schleife über Array

```vbnet
For i As Integer = 0 to myArray.LastRowIndex
  myArray(i)
Next
```

```vbnet
For Each elem As String In myArray
  ' elem
Next
```


## Arrays joinen

```vbnet
Var names() As String = Array("Anthony", "Aardvark", "Accountant")
Var combinedNames As String
combinedNames = String.FromArray(names, ",")
```


## Ein Array mit Objekten sortieren

Umsetzung: eine Methode anlegen, die zwei Instanzen *einer* Klasse vergleicht und abhängig vom Vergleich einen Integer-Wert zurückgibt. Am Beispiel einer Kundenklasse, wird eine Methode angelegt, die Objekte der Kundenklasse anhand des Nachnamens sortiert.

Methode (Beispiel):

`CustomerCompareLastName(c1 As Customer, c2 As Customer) As Integer`

```vbnet
If c1.LastName > c2.LastName Then Return 1
If c1.LastName < c2.LastName Then Return -1
Return 0
```

In dieser Sortier-Methode werden gezielt (d.h. von Hand durch den Entwickler) die Sortierregeln definiert. Als Ergebnis wird zurückgegeben:

- 1, wenn das erste Objekt "größer" als das zweite ist
- -1, wenn das zweite Objekte "größer" als das erste ist
- 0, wenn beide Objekte gleich "groß"" sind

Wenn man jetzt ein Array hat, das Elemente der Klasse (unsortiert) aufnimmt, kann man auf dem Array die Methode *Sort* verwenden und ihr die oben definierte Sortierungsmethode übergeben:

```vbnet
Customers.Sort(AddressOf CustomerCompareLastName)
```

Als Ergebnis dieses Aufrufs ist das Array bereits sortiert!







{{ feedback(page.meta.title, page.meta.section, page.meta.slug) }}
