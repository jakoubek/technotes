---
title: fenster
section: xojo
slug: windows
tags:
  - TODO
---

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


## Fenster per Escape schließen

Auf dem Fenster im Event *KeyDown*:

```vbnet
If Asc(Key) = 27 Then

  Me.Close

End If
```

Hinweis: *27* ist der ASCII-Code für die Escape-Taste.
