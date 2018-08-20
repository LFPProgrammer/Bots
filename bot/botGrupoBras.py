import telebot

bot = telebot.TeleBot("675906131:AAEUPR53yFAudLYHoX72VQDOcQpmpjbZTBM")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "Em breve responderemos!!!")


bot.polling()
