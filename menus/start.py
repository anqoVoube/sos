from telebot.types import InlineKeyboardButton, CallbackQuery

from deps import BaseMenu, MenuBot
from menus.info.start import InfoStartMenu
from menus.services.start import ServiceStartMenu
from menus.sos.start import SOSStartMenu
from static import WELCOME_TEXT


class StartMenu(BaseMenu):
    def __init__(self, bot: MenuBot):
        super().__init__(bot, WELCOME_TEXT)

    def _build_keyboard(self):
        self._keyboard.add(
            InlineKeyboardButton(
                text="SOS",
                callback_data="sos"
            ),
            InlineKeyboardButton(
                text="SERVICES",
                callback_data="services"
            ),
            InlineKeyboardButton(
                text="INFO",
                callback_data="info"
            )
        )

    @staticmethod
    def sos(callback: CallbackQuery, bot: MenuBot):
        bot.answer_callback_query(callback.id)
        bot.send_menu(callback, SOSStartMenu(bot))

    @staticmethod
    def services(callback: CallbackQuery, bot: MenuBot):
        bot.answer_callback_query(callback.id)
        bot.send_menu(callback, ServiceStartMenu(bot))

    @staticmethod
    def info(callback: CallbackQuery, bot: MenuBot):
        bot.answer_callback_query(callback.id)
        bot.send_menu(callback, InfoStartMenu(bot))

    @staticmethod
    def main_menu(callback: CallbackQuery, bot: MenuBot):
        bot.answer_callback_query(callback.id)
        bot.send_menu(callback, StartMenu(bot))

    def _build_handlers(self):
        self._bot.register_callback_query_handler(
            self.sos,
            self._bot.eq_callback("sos"),
            pass_bot=True
        )

        self._bot.register_callback_query_handler(
            self.services,
            self._bot.eq_callback("services"),
            pass_bot=True
        )

        self._bot.register_callback_query_handler(
            self.info,
            self._bot.eq_callback("info"),
            pass_bot=True
        )

        self._bot.register_callback_query_handler(
            self.main_menu,
            self._bot.eq_callback("main_menu"),
            pass_bot=True
        )
