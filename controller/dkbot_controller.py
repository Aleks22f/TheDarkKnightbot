import telebot

token = "5486480610:AAG__Eowe3JnF-QJFXSk_4vltJxWVf6IVC0"

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет!')

bot.polling()
