from contextvars import ContextVar
from typing import ClassVar

from codetable.core.code import Code


class i18n(Code):
    """
    A Code implementation that supports internationalization (i18n).

    This class allows defining messages for different locales and retrieving the
    appropriate message based on the current context locale.

    Attributes:
        _base_locale (ClassVar[str]): The default locale to fall back to if the current
            locale's message is not found.
        _current_locale (ClassVar[ContextVar[str]]): A context variable holding the
            current locale. Defaults to "codetable.locale".
    """
    _base_locale: ClassVar[str]
    _current_locale: ClassVar[ContextVar[str]] = ContextVar("codetable.locale")

    def __init__(self, **msg: str) -> None:
        """
        Initializes an i18n Code instance with messages for different locales.

        Args:
            **msg (str): Keyword arguments mapping locale codes to message strings.

        Raises:
            RuntimeError: If `_base_locale` has not been set prior to initialization.
        """
        super().__init__()

        self.msg: dict[str, str] = msg

        if not hasattr(self, "_base_locale"):
            raise RuntimeError(
                "Before the first i18n call, you must call "
                "i18n.set_base_locale() because a base locale is required."
            )

    def compute_value(self) -> str:
        """
        Computes the localized message based on the current locale.

        Returns:
            str: The message corresponding to the current locale, or the base locale
                if the current locale is not available.
        """
        localized: str = self.msg.get(
            self.get_locale(), self.msg[self.get_base_locale()]
        )

        return localized

    @classmethod
    def get_locale(cls) -> str:
        """
        Retrieves the current locale from the context.

        Returns:
            str: The current locale, or the base locale if no locale is set in the context.
        """
        return cls._current_locale.get(cls._base_locale)

    @classmethod
    def set_locale(cls, locale: str) -> None:
        """
        Sets the current locale for the context.

        Args:
            locale (str): The locale code to set (e.g., "en", "pl").
        """
        cls._current_locale.set(locale)

    @classmethod
    def get_base_locale(cls) -> str:
        """
        Retrieves the base locale.

        Returns:
            str: The base locale code.
        """
        return cls._base_locale

    @classmethod
    def set_base_locale(cls, base_locale: str) -> None:
        """
        Sets the base locale.

        Args:
            base_locale (str): The locale code to serve as the default fallback.
        """
        cls._base_locale = base_locale
