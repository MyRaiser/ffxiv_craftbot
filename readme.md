# FFXIV Craft Bot

> This repo is under reworking!

## Introduction

Do crafting automatically, with or without GUI.

> Just a toy project.

- **ATTENTION**
    **DO NOT** do crafting when you're AFK. This tool **DOES NOT** ensure proper action of character in game.

## Usage

Start with:

```py
from craftbot import Craftbot
```

- **Craftbot**(self, window_title: str, *, debug: bool = False)
    Generate a Craftbot object. This requires admin permission, if not debugging.
    - `window_title`: title of FFXIV window. Typically, do it as:
        
        ```py
        from craftbot import Craftbot
        ffxiv = Craftbot("最终幻想XIV")
        ```

- Craftbot. **run**()
    Make craftbot run.

- Craftbot. **delay**(ms: Number)
    Delay for some milliseconds, with default jitter as 5%.

- Craftbot. **press**(key: str)
    Press certain key. Specially, it supports key like `numpad_0`, `numpad_*`.

- Craftbot. **press_hwnd**(key: str)
    Press certain key in window. Specially, it supports key like `numpad_0`, `numpad_*`. 

```py
from craftbot.macro import get_macro_time
```

- **get_marco_time**(macro: str) -> int
    Calculate total time of macro.
    
## Execute

### CLI

1. Write your script, e.g. filename is `mymacro.py`.

2. Choose target recipe in crafting page. Ensure your macro is in correct key.

3. Open Powershell (with admin permission) and run:

    ```bash
    python mymacro.py
    ```

### GUI

Simply run:

```bash
python ffxiv_craftbot.pyw
```

or you can use Pyinstaller to pack it:

```bash
sh build.sh
```

