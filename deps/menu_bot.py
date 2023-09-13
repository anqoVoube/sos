from typing import Union

import redis
from telebot import TeleBot
from telebot.types import Message, CallbackQuery, InputMedia, InputMediaPhoto, InlineKeyboardButton, InlineKeyboardMarkup

r = redis.Redis(host='localhost', port=6379, decode_responses=True)


class MenuBot(TeleBot):
    def __init__(self, token: str):
        super().__init__(token)

    def send_menu(self, message: Union[CallbackQuery, Message], menu, **kwargs):
        if not isinstance(message, Message) or message.text != "/start":
            if prev_message_id := r.get(str(message.from_user.id)):
                try:
                    sent_message: Message = self.edit_message_text(
                        text=menu.message,
                        chat_id=message.from_user.id,
                        message_id=prev_message_id,
                        reply_markup=menu.keyboard,
                        **kwargs
                    )
                except:
                    self.delete_message(chat_id=message.from_user.id, message_id=prev_message_id)
                    sent_message: Message = self.send_message(message.from_user.id, menu.message,
                                                              reply_markup=menu.keyboard, **kwargs)
            else:
                sent_message: Message = self.send_message(message.from_user.id, menu.message, reply_markup=menu.keyboard, **kwargs)
        else:
            sent_message: Message = self.send_message(message.from_user.id, menu.message, reply_markup=menu.keyboard,
                                                      **kwargs)
        r.set(str(message.from_user.id), str(sent_message.id), ex=1000)

    def replace_menu(self, message_id: int, message: Union[CallbackQuery, Message], menu, **kwargs):
        self.edit_message_text(menu.message, message.from_user.id, message_id, reply_markup=menu.keyboard, **kwargs)
        # self.send_message(message.from_user.id, menu.message, reply_markup=menu.keyboard, **kwargs)
    def in_callback(self, callback_string: str):
        return lambda callback: callback_string in callback.data

    def send_replaced_photo(self, back, chat_id, photo, caption):
        self.delete_message(chat_id=chat_id, message_id=r.get(str(chat_id)))
        keyboard = InlineKeyboardMarkup(row_width=1)
        keyboard.add(InlineKeyboardButton(text="Назад", callback_data=back),)
        message = self.send_photo(chat_id=chat_id, photo=photo, caption=caption, reply_markup=keyboard)
        r.set(str(chat_id), str(message.id))

    def eq_callback(self, callback_string: str):
        return lambda callback: callback_string == callback.data
