from typing import Union

from telebot import TeleBot
from telebot.types import Message, CallbackQuery


class MenuBot(TeleBot):
    def __init__(self, token: str):
        super().__init__(token)

    def send_menu(self, message: Union[CallbackQuery, Message], menu, **kwargs):
        self.send_message(message.from_user.id, menu.message, reply_markup=menu.keyboard, **kwargs)

    def replace_menu(self, message_id: int, message: Union[CallbackQuery, Message], menu, **kwargs):
        self.edit_message_text(menu.message, message.from_user.id, message_id, reply_markup=menu.keyboard, **kwargs)
        # self.send_message(message.from_user.id, menu.message, reply_markup=menu.keyboard, **kwargs)

    def in_callback(self, callback_string: str):
        return lambda callback: callback_string in callback.data

    def eq_callback(self, callback_string: str):
        return lambda callback: callback_string == callback.data
