---
title: Dialoge in Xojo
section: xojo
slug: dialog
---

# Dialoge in Xojo


## MessageDialog

```basic
Var d As New MessageDialog
Var b As MessageDialogButton

d.icon = MessageDialog.GraphicQuestion
d.ActionButton.Caption = "Ja, jetzt drucken"
d.CancelButton.Caption = "Abbrechen"
d.CancelButton.Visible = True
d.Message = "Möchten Sie den Druckprozess jetzt starten?"

b = d.ShowModal

If b = d.ActionButton Then
End If
```


## SaveFileDialog

```vbnet
Var dlg As New SaveFileDialog
Var saveFile As FolderItem
dlg.InitialFolder = SpecialFolder.Documents
dlg.PromptText = "Prompt Text"
dlg.SuggestedFileName = "Suggested Filename"
dlg.Title = "Title Property"
// defined as a file type in FileTypeGroup1 file type set
dlg.Filter = FileTypeGroup1.Text
saveFile = dlg.ShowModal
If saveFile <> Nil Then
  // saveFile is the FolderItem of the file to save
Else
  // user canceled
End If
```


{{ feedback(page.meta.title, page.meta.section, page.meta.slug) }}
