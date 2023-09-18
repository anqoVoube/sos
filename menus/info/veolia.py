from telebot.types import InlineKeyboardButton, CallbackQuery

from deps import BaseMenu, MenuBot
from static import VEOLIA_TEXT


class InfoVeoliaMenu(BaseMenu):
    def __init__(self, bot: MenuBot):
        super().__init__(bot, VEOLIA_TEXT)

    def _build_keyboard(self):
        self._keyboard.add(
            InlineKeyboardButton(
                text="что такое Veolia",
                callback_data="info_what_veolia"
            ),
            InlineKeyboardButton(
                text="местоположение",
                callback_data="info_location_veolia"
            ),
            InlineKeyboardButton(
                text="сотрудники Veolia",
                callback_data="info_workers_veolia"
            ),
            InlineKeyboardButton(
                text="Назад",
                callback_data="info"
            )
        )

    @staticmethod
    def what_is_veolia(callback: CallbackQuery, bot: MenuBot):
        bot.answer_callback_query(callback.id)
        bot.send_message(callback.from_user.id, "lorem22")

    @staticmethod
    def veolia_location(callback: CallbackQuery, bot: MenuBot):
        bot.answer_callback_query(callback.id)
        bot.send_message(callback.from_user.id, "локацию скинет")

    @staticmethod
    def veolia_workers(callback: CallbackQuery, bot: MenuBot):
        bot.answer_callback_query(callback.id)
        bot.send_message(callback.from_user.id, """Миразизов Алишер Авазович
Ведущий инженер
+998991234567
""")

    def _build_handlers(self):
        self._bot.register_callback_query_handler(
            self.what_is_veolia,
            self._bot.eq_callback("info_what_veolia"),
            pass_bot=True
        )

        self._bot.register_callback_query_handler(
            self.veolia_location,
            self._bot.eq_callback("info_location_veolia"),
            pass_bot=True
        )

        self._bot.register_callback_query_handler(
            self.veolia_workers,
            self._bot.eq_callback("info_workers_veolia"),
            pass_bot=True
        )
