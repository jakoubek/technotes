# Dictionaries in Xojo


## Dictionary anlegen und Werte zuweisen

```vbnet
Var myDict As New Dictionary

myDict.Value("Key") = "my value"
myDict.Value("Key2") = "my value #2"
```


## Dictionary in Array überführen

```vbnet
Var myArray() As String

For Each key As Variant In myDict.Keys
  Var theValue As String = myDict.Value(key)
  myArray.AddRow(theValue)
Next
```

