# Fenster


## Fenster zentrieren

```vbnet
MainWindow.Left = (Screen(0).Width - MainWindow.Width) / 2
MainWindow.Top = (Screen(0).Height - MainWindow.Height) / 2
```


## Fenster maximieren

Im Event Handler *Open*:

```vbnet
Me.Maximize
```

