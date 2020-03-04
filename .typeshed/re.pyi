import enum
from typing import Any

class RegexFlag(enum.IntFlag):
    ASCII: Any = ...
    A: Any = ...
    IGNORECASE: Any = ...
    I: Any = ...
    LOCALE: Any = ...
    L: Any = ...
    UNICODE: Any = ...
    U: Any = ...
    MULTILINE: Any = ...
    M: Any = ...
    DOTALL: Any = ...
    S: Any = ...
    VERBOSE: Any = ...
    X: Any = ...
    TEMPLATE: Any = ...
    T: Any = ...
    DEBUG: Any = ...

error: Any

# def match(pattern: Any, string: Any, flags: int = ...): ...
# def fullmatch(pattern: Any, string: Any, flags: int = ...): ...
def search(pattern: Any, string: Any, flags: int = ...) -> Match: ...

# def sub(pattern: Any, repl: Any, string: Any, count: int = ..., flags: int = ...): ...
# def subn(pattern: Any, repl: Any, string: Any, count: int = ..., flags: int = ...): ...
# def split(pattern: Any, string: Any, maxsplit: int = ..., flags: int = ...): ...
# def findall(pattern: Any, string: Any, flags: int = ...): ...
# def finditer(pattern: Any, string: Any, flags: int = ...): ...
# def compile(pattern: Any, flags: int = ...): ...
# def purge() -> None: ...
# def template(pattern: Any, flags: int = ...): ...
# def escape(pattern: Any): ...

Pattern: Any
Match: Any

# class Scanner:
#     lexicon: Any = ...
#     scanner: Any = ...
#     def __init__(self, lexicon: Any, flags: int = ...) -> None: ...
#     match: Any = ...
#     def scan(self, string: Any): ...

# Names in __all__ with no definition:
#   A
#   ASCII
#   DOTALL
#   I
#   IGNORECASE
#   L
#   LOCALE
#   M
#   MULTILINE
#   S
#   U
#   UNICODE
#   VERBOSE
#   X