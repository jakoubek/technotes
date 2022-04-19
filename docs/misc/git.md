---
tags:
  - TODO
---

# Git

## Datei umbenennen

Wenn man eine Datei, die bereits Teil eines Repositorys ist, umbenennen möchte, dann sollte man das über die eingebaute Git-Funktionalität machen. Wenn man die Datei einfach über das Dateisystem (z.B. Explorer) umbenennt, dann *verschwindet* die ursprüngliche Datei samt Historie und eine neue, zusätzliche Datei wird hinzugefügt. Beim Umbenennen über Git bleibt die Historie erhalten.

```shell
git mv alterdateiname neuerdateiname
```

Anschließend muss die Änderung committet werden.

