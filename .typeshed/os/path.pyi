from genericpath import *
from typing import Any, Optional

curdir: str
pardir: str
extsep: str
sep: str
pathsep: str
defpath: str
altsep: Any
devnull: str

def normcase(s: Any): ...
def isabs(s: Any): ...
def join(a: Any, *p: Any): ...
def split(p: Any): ...
def splitext(p: Any): ...
def splitdrive(p: Any): ...
def basename(p: Any): ...
def dirname(p: Any): ...
def islink(path: Any): ...
def lexists(path: Any): ...
def ismount(path: Any): ...
def expanduser(path: Any): ...
def expandvars(path: Any): ...
def normpath(path: Any): ...
def abspath(path: Any): ...
def realpath(filename: Any): ...

supports_unicode_filenames: Any

def relpath(path: Any, start: Optional[Any] = ...): ...
def commonpath(paths: Any): ...

# Names in __all__ with no definition:
#   commonprefix
#   exists
#   getatime
#   getctime
#   getmtime
#   getsize
#   isdir
#   isfile
#   samefile
#   sameopenfile
#   samestat
