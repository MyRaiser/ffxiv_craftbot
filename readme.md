# FFXIV Craft Bot
## Introduction

Do crafting automatically, support normal crafting, multiple macros crafting, collection crafting.

Start with:

```py
from ffxiv_craftbot import Macro, Craftbot
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
        ffxiv = Craftbot('最终幻想XIV')
        ```

- `Craftbot.forge(*macros, rst_macro_key, is_collection)`
    do crafting(once).
    - `macros`: macros to execute.
    - `rst_macro_key`: Key of rst_macro. Make a macro in FFXIV to interrupt all macros. This can improve stability. Default None.
    - `is_collection`: whether to do the additional collection confirmation step. Default False.

## Sample Code

```py
from ffxiv_craftbot import Macro, Craftbot

macro1_content =\
"""
/ac 闲静 <wait.3>
/ac 掌握 <wait.2>
/ac 改革 <wait.2>
/ac 精密制作 <wait.3>
/ac 精密制作 <wait.3>
/ac 阔步 <wait.2>
/ac 比尔格的祝福 <wait.3>
/ac 精密制作 <wait.3>
"""
macro1 = Macro(macro1_content, '4')

ffxiv = Craftbot('最终幻想XIV')
ffxiv.forge(macro1, rst_macro_key='`', is_collection=True)



```