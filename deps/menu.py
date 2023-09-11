from abc import ABC, abstractmethod
from typing import Optional

from telebot.types import InlineKeyboardMarkup

from deps import MenuBot


class BaseMenu(ABC):
    def __init__(self, bot: MenuBot, message: Optional[str] = None, row_width: int = 1):
        self._bot = bot
        self._message = message or "Text is coming soon..."
        self._keyboard = InlineKeyboardMarkup(row_width=row_width)
        self._build_keyboard()
        self._build_handlers()

    @property
    def keyboard(self):
        return self._keyboard

    @property
    def message(self):
        return self._message

    @abstractmethod
    def _build_keyboard(self):
        pass

    @abstractmethod
    def _build_handlers(self):
        pass
