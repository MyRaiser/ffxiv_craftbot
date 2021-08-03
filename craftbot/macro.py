import re


def get_marco_time(macro: str) -> int:
    """find all nums and sum. return seconds."""
    pattern = "[1-9]"
    result = re.findall(pattern, macro, flags=0)
    t = sum((int(x) for x in result))
    # report("Macro length:", t, "sec")
    return t


class Macro:
    """
    generate a macro object used in `Craftbot.forge()`. Time will be calculated automatically.
    :param macro: macro content text.
    :param key: macro shortcut key.
    """

    def __init__(self, macro, key):
        self.macro = macro
        self.key = key
        self.time = get_marco_time(self.macro)

    def __repr__(self):
        return self.macro+"\nkey:"+self.key+"\ntime:"+str(self.time)
