from telebot.types import Message

from config.settings import TOKEN
from deps import MenuBot
from menus import StartMenu

bot = MenuBot(token=TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome(message: Message):
    bot.send_menu(message, StartMenu(bot))


bot.infinity_polling()
