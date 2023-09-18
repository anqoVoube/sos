from telebot.types import InlineKeyboardButton, CallbackQuery

from deps import BaseMenu, MenuBot
from static import SUVSOZ_TEXT


class InfoSuvSozMenu(BaseMenu):
    def __init__(self, bot: MenuBot):
        super().__init__(bot, SUVSOZ_TEXT)

    def _build_keyboard(self):
        self._keyboard.add(
            InlineKeyboardButton(
                text="что такое СУВСОЗ",
                callback_data="info_what_suvsoz"
            ),
            InlineKeyboardButton(
                text="местоположение",
                callback_data="info_location_suvsoz"
            ),
            InlineKeyboardButton(
                text="сотрудники СУВСОЗ",
                callback_data="info_workers_suvsoz"
            ),
            InlineKeyboardButton(
                text="Назад",
                callback_data="info"
            )
        )

    @staticmethod
    def what_is_suvsoz(callback: CallbackQuery, bot: MenuBot):
        bot.answer_callback_query(callback.id)
        bot.send_message(callback.from_user.id, "lorem22")

    @staticmethod
    def suvsoz_location(callback: CallbackQuery, bot: MenuBot):
        bot.answer_callback_query(callback.id)
        bot.send_message(callback.from_user.id, "локацию скинет")

    @staticmethod
    def suvsoz_workers(callback: CallbackQuery, bot: MenuBot):
        bot.answer_callback_query(callback.id)
        bot.send_message(callback.from_user.id, """Миразизов Алишер Авазович
Ведущий инженер
+998991234567
""")

    def _build_handlers(self):
        self._bot.register_callback_query_handler(
            self.what_is_suvsoz,
            self._bot.eq_callback("info_what_suvsoz"),
            pass_bot=True
        )

        self._bot.register_callback_query_handler(
            self.suvsoz_location,
            self._bot.eq_callback("info_location_suvsoz"),
            pass_bot=True
        )

        self._bot.register_callback_query_handler(
            self.suvsoz_workers,
            self._bot.eq_callback("info_workers_suvsoz"),
            pass_bot=True
        )
