from typing import Any, Optional

PRETEND_KEY: str
TEMPLATES: Any

def get_version(
    root: str = ...,
    version_scheme: Any = ...,
    local_scheme: Any = ...,
    write_to: Optional[Any] = ...,
    write_to_template: Optional[Any] = ...,
    relative_to: Optional[Any] = ...,
    tag_regex: Any = ...,
    fallback_version: Optional[Any] = ...,
    fallback_root: str = ...,
    parse: Optional[Any] = ...,
    git_describe_command: Optional[Any] = ...,
) -> str: ...
