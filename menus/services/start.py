from telebot.types import InlineKeyboardButton, CallbackQuery

from deps import BaseMenu, MenuBot
from static import WELCOME_TEXT


class ServiceStartMenu(BaseMenu):
    def __init__(self, bot: MenuBot):
        super().__init__(bot, WELCOME_TEXT)

    def _build_keyboard(self):
        self._keyboard.add(
            InlineKeyboardButton(
                text="Подать заявку",
                callback_data="services_unknown"
            ),
            InlineKeyboardButton(
                text="активные заявки",
                callback_data="services_actives"
            ),
            InlineKeyboardButton(
                text="история заявок",
                callback_data="services_history"
            ),
            InlineKeyboardButton(
                text="данные о пользователе",
                callback_data="services_data"
            ),
            InlineKeyboardButton(
                text="Назад",
                callback_data="main_menu"
            )
        )

    @staticmethod
    def unknown(callback: CallbackQuery, bot: MenuBot):
        bot.answer_callback_query(callback.id)

        from menus.services.unknown import ServiceUnknownMenu

        bot.send_menu(callback, ServiceUnknownMenu(bot))

    @staticmethod
    def active(callback: CallbackQuery, bot: MenuBot):
        bot.answer_callback_query(callback.id)
        bot.send_message(callback.from_user.id, "Next step is not presented in Miro :D")

    @staticmethod
    def history(callback: CallbackQuery, bot: MenuBot):
        bot.answer_callback_query(callback.id)
        bot.send_message(callback.from_user.id, "Next step is not presented in Miro :D")

    @staticmethod
    def data(callback: CallbackQuery, bot: MenuBot):
        bot.answer_callback_query(callback.id)
        bot.send_message(callback.from_user.id, "Next step is not presented in Miro :D")

    def _build_handlers(self):
        self._bot.register_callback_query_handler(
            self.unknown,
            self._bot.eq_callback("services_unknown"),
            pass_bot=True
        )

        self._bot.register_callback_query_handler(
            self.active,
            self._bot.eq_callback("services_active"),
            pass_bot=True
        )

        self._bot.register_callback_query_handler(
            self.history,
            self._bot.eq_callback("services_history"),
            pass_bot=True
        )

        self._bot.register_callback_query_handler(
            self.data,
            self._bot.eq_callback("services_data"),
            pass_bot=True
        )
