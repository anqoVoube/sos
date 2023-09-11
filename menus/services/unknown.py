from telebot.types import InlineKeyboardButton, CallbackQuery

from deps import BaseMenu, MenuBot
from static import UNKNOWN_TEXT, SEND_REPORT


class ServiceUnknownMenu(BaseMenu):
    def __init__(self, bot: MenuBot):
        super().__init__(bot, UNKNOWN_TEXT)

    def _build_keyboard(self):
        self._keyboard.add(
            InlineKeyboardButton(
                text="РЭС(Районные электрические сети)",
                callback_data="services_unknown_res"
            ),
            InlineKeyboardButton(
                text="СУВСОЗ(холодная вода)",
                callback_data="services_unknown_suvsoz"
            ),
            InlineKeyboardButton(
                text="Veolia Energy(горячая вода отопления)",
                callback_data="services_unknown_veolia"
            ),
            InlineKeyboardButton(
                text="Назад",
                callback_data="services_menu"
            ),
        )

    @staticmethod
    def res(callback: CallbackQuery, bot: MenuBot):
        bot.answer_callback_query(callback.id)
        bot.send_message(
            callback.from_user.id,
            SEND_REPORT
        )

    @staticmethod
    def suvsoz(callback: CallbackQuery, bot: MenuBot):
        bot.answer_callback_query(callback.id)
        bot.send_message(
            callback.from_user.id,
            SEND_REPORT
        )

    @staticmethod
    def veolia(callback: CallbackQuery, bot: MenuBot):
        bot.answer_callback_query(callback.id)
        bot.send_message(
            callback.from_user.id,
            SEND_REPORT
        )

    def _build_handlers(self):
        self._bot.register_callback_query_handler(
            self.res,
            self._bot.eq_callback("services_unknown_res"),
            pass_bot=True
        )

        self._bot.register_callback_query_handler(
            self.suvsoz,
            self._bot.eq_callback("services_unknown_suvsoz"),
            pass_bot=True
        )

        self._bot.register_callback_query_handler(
            self.veolia,
            self._bot.eq_callback("services_unknown_veolia"),
            pass_bot=True
        )
