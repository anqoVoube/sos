from telebot.types import InlineKeyboardButton, CallbackQuery

from deps import BaseMenu, MenuBot
from menus.info.res import InfoResMenu
from menus.info.suvsoz import InfoSuvSozMenu
from menus.info.veolia import InfoVeoliaMenu
from static import WELCOME_TEXT


class InfoStartMenu(BaseMenu):
    def __init__(self, bot: MenuBot):
        super().__init__(bot, WELCOME_TEXT)

    def _build_keyboard(self):
        self._keyboard.add(
            InlineKeyboardButton(
                text="подробнее о РЭС(Районные электрические сети)",
                callback_data="info_res"
            ),
            InlineKeyboardButton(
                text="подробнее о СУВСОЗ",
                callback_data="info_suvsoz"
            ),
            InlineKeyboardButton(
                text="подробнее о Veolia Energy",
                callback_data="info_veolia"
            ),
            InlineKeyboardButton(
                text="Назад",
                callback_data="main_menu"
            )
        )

    @staticmethod
    def res(callback: CallbackQuery, bot: MenuBot):
        bot.answer_callback_query(callback.id)
        bot.send_menu(callback, InfoResMenu(bot))

    @staticmethod
    def suvsoz(callback: CallbackQuery, bot: MenuBot):
        bot.answer_callback_query(callback.id)
        bot.send_menu(callback, InfoSuvSozMenu(bot))

    @staticmethod
    def veolia(callback: CallbackQuery, bot: MenuBot):
        bot.answer_callback_query(callback.id)
        bot.send_menu(callback, InfoVeoliaMenu(bot))

    def _build_handlers(self):
        self._bot.register_callback_query_handler(
            self.res,
            self._bot.eq_callback("info_res"),
            pass_bot=True
        )

        self._bot.register_callback_query_handler(
            self.suvsoz,
            self._bot.eq_callback("info_suvsoz"),
            pass_bot=True
        )

        self._bot.register_callback_query_handler(
            self.veolia,
            self._bot.eq_callback("info_veolia"),
            pass_bot=True
        )

        self._bot.register_callback_query_handler(
            self.veolia,
            self._bot.eq_callback("info"),
            pass_bot=True
        )
