from telebot.types import InlineKeyboardButton, CallbackQuery, Message, InlineKeyboardMarkup, ReplyKeyboardMarkup, \
    KeyboardButton

from config.settings import ADMIN_ID
from deps import BaseMenu, MenuBot
from deps.menu_bot import r
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
                callback_data="services"
            ),
        )

    @staticmethod
    def res(callback: CallbackQuery, bot: MenuBot):
        bot.answer_callback_query(callback.id)
        message = bot.send_message(
            callback.from_user.id,
            SEND_REPORT
        )
        bot.register_next_step_handler(message, ServiceUnknownMenu.phone, bot)

    @staticmethod
    def suvsoz(callback: CallbackQuery, bot: MenuBot):
        bot.answer_callback_query(callback.id)
        message = bot.send_message(
            callback.from_user.id,
            SEND_REPORT
        )
        bot.register_next_step_handler(message, ServiceUnknownMenu.phone, bot)

    @staticmethod
    def veolia(callback: CallbackQuery, bot: MenuBot):
        bot.answer_callback_query(callback.id)
        message = bot.send_message(
            callback.from_user.id,
            SEND_REPORT
        )
        bot.register_next_step_handler(message, ServiceUnknownMenu.phone, bot)

    @staticmethod
    def phone(message, bot):
        keyboard = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)  # Connect the keyboard
        button_phone = KeyboardButton(text="Send phone", request_contact=True)  # Specify the name of the button that the user will see
        keyboard.add(button_phone)  # Add this button
        prev_message = bot.send_message(
            message.chat.id,
            'Phone number',
            reply_markup=keyboard
        )
        bot.register_next_step_handler(prev_message, ServiceUnknownMenu.final, bot, message.text)

    @staticmethod
    def final(message: Message, bot: MenuBot, message_text):
        bot.send_message(chat_id=ADMIN_ID, text=f"{message.contact.phone_number}\n{message_text}")
        keyboard = InlineKeyboardMarkup(row_width=1)
        keyboard.add(InlineKeyboardButton(text="Назад", callback_data="services"))
        prev_message = bot.send_message(chat_id=message.from_user.id, text="Доставлено!", reply_markup=keyboard)
        r.set(str(message.from_user.id), str(prev_message.id))

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
