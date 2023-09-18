from telebot.types import InlineKeyboardButton, CallbackQuery

from deps import BaseMenu, MenuBot
from static import RES_TEXT


class InfoResMenu(BaseMenu):
    def __init__(self, bot: MenuBot):
        super().__init__(bot, RES_TEXT)

    def _build_keyboard(self):
        self._keyboard.add(
            InlineKeyboardButton(
                text="что такое РЭС",
                callback_data="info_what_res"
            ),
            InlineKeyboardButton(
                text="местоположение",
                callback_data="info_location_res"
            ),
            InlineKeyboardButton(
                text="сотрудники РЭС",
                callback_data="info_workers_res"
            ),
            InlineKeyboardButton(
                text="Назад",
                callback_data="info"
            )
        )

    @staticmethod
    def what_is_res(callback: CallbackQuery, bot: MenuBot):
        bot.answer_callback_query(callback.id)
        bot.send_message(callback.from_user.id, "lorem22")

    @staticmethod
    def res_location(callback: CallbackQuery, bot: MenuBot):
        bot.answer_callback_query(callback.id)
        bot.send_message(callback.from_user.id, "локацию скинет")

    @staticmethod
    def res_workers(callback: CallbackQuery, bot: MenuBot):
        bot.answer_callback_query(callback.id)
        bot.send_message(callback.from_user.id, """Миразизов Алишер Авазович
Ведущий инженер
+998991234567
""")

    def _build_handlers(self):
        self._bot.register_callback_query_handler(
            self.what_is_res,
            self._bot.eq_callback("info_what_res"),
            pass_bot=True
        )

        self._bot.register_callback_query_handler(
            self.res_location,
            self._bot.eq_callback("info_location_res"),
            pass_bot=True
        )

        self._bot.register_callback_query_handler(
            self.res_workers,
            self._bot.eq_callback("info_workers_res"),
            pass_bot=True
        )
