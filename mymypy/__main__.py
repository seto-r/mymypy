import sys

from mypy.main import main


def console_entry() -> None:
    main(None, sys.stdout, sys.stderr)
