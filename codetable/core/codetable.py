from typing import ClassVar

from codetable.core.resources.types import KeyMap


class Codetable:
    """
    A base class representing a Codetable, which serves as a namespace for standardizing codes.

    Attributes:
        NAMESPACE (ClassVar[str]): The namespace identifier for the Codetable.
        key_map (KeyMap): A mapping dictionary that defines the keys for 'code' and 'value'
            in the output dictionary. Defaults to map "code" to "code" and "value" to "msg".
    """

    NAMESPACE: ClassVar[str]

    key_map: KeyMap = {"code": "code", "value": "msg"}
