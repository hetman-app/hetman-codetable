from typing import TypedDict


class KeyMap(TypedDict):
    code: str
    value: str


CodeResult = dict[str, str]
