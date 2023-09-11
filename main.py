from telebot.types import Message, KeyboardButton, ReplyKeyboardMarkup

from deps import MenuBot
from menus import StartMenu

bot = MenuBot(token="6391896963:AAErxWgKqyOoXAWCZpJntR1OB82yT5_CPWM")


@bot.message_handler(commands=['start'])
def send_welcome(message: Message):
    bot.send_menu(message, StartMenu(bot))


bot.infinity_polling()
