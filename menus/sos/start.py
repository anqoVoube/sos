from telebot.types import InlineKeyboardButton, CallbackQuery

from deps import BaseMenu, MenuBot
from static import CHOSE_SOS_OPTIONS

UCHASTKOVIY = "uchastkoviy"
SANTEXNIK = "santexnik"
ELECTRIC = "electric"
LIFTER = "lifter"


class SOSStartMenu(BaseMenu):
    def __init__(self, bot: MenuBot):
        super().__init__(bot, CHOSE_SOS_OPTIONS)

    def _build_keyboard(self):
        self._keyboard.add(
            InlineKeyboardButton(
                text="Дежурный номер участковый",
                callback_data=f"sos_{UCHASTKOVIY}"
            ),
            InlineKeyboardButton(
                text="Дежурный номер сантехник",
                callback_data=f"sos_{SANTEXNIK}"
            ),
            InlineKeyboardButton(
                text="Дежурный номер электрик",
                callback_data=f"sos_{ELECTRIC}"
            ),
            InlineKeyboardButton(
                text="Дежурный номер лифтёр",
                callback_data=f"sos_{LIFTER}"
            ),
            InlineKeyboardButton(
                text="Назад",
                callback_data="main_menu"
            )
        )

    @staticmethod
    def uchastkoviy(callback: CallbackQuery, bot: MenuBot):
        bot.answer_callback_query(callback.id)
        with open("media/sashka.jpg", "rb") as file:
            bot.send_replaced_photo("sos", callback.from_user.id, file, f"+998(94) 671-09-50\nСаша Артёмов\n{UCHASTKOVIY}")

    @staticmethod
    def santexnik(callback: CallbackQuery, bot: MenuBot):
        bot.answer_callback_query(callback.id)
        with open("media/sashka.jpg", "rb") as file:
            bot.send_replaced_photo("sos", callback.from_user.id, file, f"+998(94) 671-09-50\nСаша Артёмов\n{UCHASTKOVIY}")


    @staticmethod
    def electric(callback: CallbackQuery, bot: MenuBot):
        bot.answer_callback_query(callback.id)
        with open("media/sashka.jpg", "rb") as file:
            bot.send_replaced_photo("sos", callback.from_user.id, file, f"+998(94) 671-09-50\nСаша Артёмов\n{UCHASTKOVIY}")


    @staticmethod
    def lifter(callback: CallbackQuery, bot: MenuBot):
        bot.answer_callback_query(callback.id)
        with open("media/sashka.jpg", "rb") as file:
            bot.send_replaced_photo("sos", callback.from_user.id, file, f"+998(94) 671-09-50\nСаша Артёмов\n{UCHASTKOVIY}")

    def _build_handlers(self):
        self._bot.register_callback_query_handler(
            self.uchastkoviy,
            self._bot.eq_callback(f"sos_{UCHASTKOVIY}"),
            pass_bot=True
        )

        self._bot.register_callback_query_handler(
            self.santexnik,
            self._bot.eq_callback(f"sos_{SANTEXNIK}"),
            pass_bot=True
        )

        self._bot.register_callback_query_handler(
            self.electric,
            self._bot.eq_callback(f"sos_{ELECTRIC}"),
            pass_bot=True
        )

        self._bot.register_callback_query_handler(
            self.lifter,
            self._bot.eq_callback(f"sos_{LIFTER}"),
            pass_bot=True
        )
