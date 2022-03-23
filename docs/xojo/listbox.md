# Listbox / DesktopListbox

## Prüfen, ob überhaupt eine Zeile ausgewählt ist

**Single-Select!**

```vbnet
If Me.SelectedRowIndex <> Listbox.NoSelection Then
  
End If
```

## Über Zeilen einer Listbox iterieren

```vbnet
For Each row As ListboxRow In lstObjekte.Rows
  
Next
```

oder

```vbnet
For i As Integer = 0 To lstObjekte.LastRowIndex

Next
```

## Listbox sortieren

### individuelle Sortierung für eine Spalte

- es muss das Ereignis **CompareRows** für die Listbox verwendet werden
- sinnvollerweise wird im **CellTag** der Spalte ein numerisches Attribut versteckt, auf das für die Suche zugegriffen werden kann

```vbnet
Select Case column
Case 2
    If Val(Me.CellTag(row1, column)) < Val(Me.CellTag(row2, column)) Then
        result = -1
    Elseif Val(Me.CellTag(row1, column)) > Val(Me.CellTag(row2, column)) Then
        result = 1
    Else
        result = 0
    End If
    Return True
Case Else
    Return False
End Select
```
