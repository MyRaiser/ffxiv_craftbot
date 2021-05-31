# FFXIV Craft Bot
## Introduction

Do crafting automatically, support normal crafting, multiple macros crafting, collection crafting.

- **ATTENTION**
    **DO NOT** do crafting when you're AFK. Please stay in front of your PC and monitor when running. This tool is only to free your hand from boring work. This tool **DOES NOT** ensure proper action of character in game.

Start with:

```py

from craftbot.macro import Macro
from craftbot.craftbot import Craftbot
```

## Usage
- `Macro(macro, key)`
    generate a macro object used in `Craftbot.forge()`. Time will be calculated automatically.
    - `macro`: macro content text.
    - `key`: macro shortcut key.

- `Craftbot(window_title)`
    generate a Craftbot object.
    - `window_title`: title of FFXIV window. Typically, do it as:
        
        ```py
        from craftbot import Craftbot
        ffxiv = Craftbot("最终幻想XIV")
        ```

- `Craftbot.forge(*macros, rst_macro_key, is_collection)`
    do crafting(once).
    - `macros`: macros to execute.
    - `rst_macro_key`: Key of rst_macro. Make a macro in FFXIV to interrupt all macros. This can improve stability. Default None.
    - `is_collection`: whether to do the additional collection confirmation step. Default False.

## Sample Code

```py

from craftbot.macro import Macro
from craftbot.craftbot import Craftbot

macro1_content ="""/ac 闲静 <wait.3>
/ac 掌握 <wait.2>
/ac 改革 <wait.2>
/ac 精密制作 <wait.3>
/ac 精密制作 <wait.3>
/ac 阔步 <wait.2>
/ac 比尔格的祝福 <wait.3>
/ac 精密制作 <wait.3>"""

macro1 = Macro(macro1_content, '4')

ffxiv = Craftbot('最终幻想XIV')
ffxiv.forge(macro1, rst_macro_key='`', is_collection=True)
```

## Execute

### Command Line
1. Write your script. (e.g. filename is `mymacro.py`)

2. Choose target recipe in crafting page. Ensure your macro is in correct key.

3. Open Powershell(with Admin permission) and run:
    ```bash
    python mymacro.py
    ```

### GUI
run:
```bash
python ffxiv_craftbot.pyw
```

or you can use Pyinstaller to pack it and run `GUI.exe`