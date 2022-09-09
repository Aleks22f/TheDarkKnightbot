import telebot
from utils import read_config
from telebot import types

token = read_config(read_config("config/config.json")["bot_api_key"])

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет! Прокинь ФИО')


@bot.message_handler(commands=['hui'])
def fio(message):
    markup_inline = types.InlineKeyboardMarkup()
    pohui = types.InlineKeyboardButton(text='ПОЛОЖИТЬ ХУЙ', callback_data='ВЫ ТОЛЬКО ЧТО ПОЛОЖИЛИ НА ВСЕ ХУЙ))')
    markup_inline.add(pohui)


bot.polling()
