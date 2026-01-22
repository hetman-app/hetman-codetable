from __future__ import annotations

from typing import TYPE_CHECKING, Callable

from codetable.core.resources.types import CodeResult

if TYPE_CHECKING:
    from typing import Any, ClassVar

    from .resources.types import KeyMap


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

    @classmethod
    def lazy(cls, code: str) -> Callable[[], CodeResult]:
        """
        Creates a deferred evaluator for a specific code instance.

        This method retrieves a Code instance from the class dictionary and returns 
        a callable that, when invoked, triggers the actual data retrieval or 
        computation (via the `__get__` descriptor protocol).

        Args:
            code: The string key representing the attribute name of the 
                Code instance to be lazily loaded.

        Returns:
            A zero-argument callable that returns a `CodeResult` when called.

        Raises:
            RuntimeError: If the attribute associated with `code` is not an 
                instance of the `Code` class.
        """
        from codetable.core.code import Code

        instance: Any = cls.__dict__.get(code)

        if not isinstance(instance, Code):
            raise RuntimeError("Code instances can only be lazy loaded.")

        return lambda: instance.__get__()
