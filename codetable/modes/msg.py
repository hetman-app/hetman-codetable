from codetable.core.code import Code


class msg(Code):
    """
    A Code implementation for static messages.

    This class represents a simple, non-localized message.
    """

    def __init__(self, msg: str, /) -> None:
        """
        Initializes a msg Code instance.

        Args:
            msg (str): The static message string.
        """
        super().__init__()

        self.msg: str = msg

    def compute_value(self) -> str:
        """
        Returns the static message.

        Returns:
            str: The stored message string.
        """
        return self.msg
