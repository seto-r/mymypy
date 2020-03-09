from importlib.metadata import PackageNotFoundError, version


def _get_version() -> str:
    try:
        return version(__name__)
    except PackageNotFoundError:
        return ""


__copyright__ = "Copyright (C) 2018 Ryunosuke Seto"
__version__ = _get_version()
__license__ = "MIT License"
__author__ = "Seto Ryunosuke"
__author_email__ = "theshootingstar@hotmail.co.jp"
__url__ = "http://github.com/seto-r/mymypy"
