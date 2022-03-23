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


