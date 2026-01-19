from abc import ABC, abstractmethod

from codetable.core.codetable import Codetable


class Code(ABC):
    """
    An abstract base class for defining codes within a Codetable.

    This class implements the descriptor protocol to automatically bind to a `Codetable`
    subclass and a variable name.
    """

    def __init__(self) -> None:
        """Initializes a new Code instance."""
        self.codetable: type[Codetable] | None = None
        self.variable_name: str | None = None

    def __set_name__(
        self, codetable: type[Codetable], variable_name: str
    ) -> None:
        """
        Binds the Code instance to a Codetable class and a variable name.

        Args:
            codetable (type[Codetable]): The Codetable class owning this attribute.
            variable_name (str): The name of the attribute in the Codetable class.
        """
        self.codetable = codetable
        self.variable_name = variable_name

    def __get__(self, *_) -> dict[str, str]:
        """
        Retrieves the code definitions when accessed on the Codetable class or instance.

        Returns:
            dict[str, str]: A dictionary containing the 'code' and its computed 'value'.
                The keys are determined by the `Codetable.key_map`.

        Raises:
            RuntimeError: If the code has not been properly bound to a Codetable.
        """
        if not self.codetable or not self.variable_name:
            raise RuntimeError(
                "There is no 'codetable' attribute or 'variable_name'."
            )

        code: str = f"{self.codetable.NAMESPACE}.{self.variable_name}".lower()

        value: str = self.compute_value()

        return {
            self.codetable.key_map["code"]: code,
            self.codetable.key_map["value"]: value
        }

    @abstractmethod
    def compute_value(self) -> str:
        """
        Computes the value associated with this code.

        Returns:
            str: The computed value of the code.
        """
        ...
