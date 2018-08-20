import telegram
from telegram.ext import Updater
from telegram.ext import CommandHandler

updater = Updater(token=''
#bot = telegram.Bot(token='675906131:AAEUPR53yFAudLYHoX72VQDOcQpmpjbZTBM')

def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Hello, that is a test!!")


start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

updater.start_polling()
#print(bot.get_me())



