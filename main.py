import telebot

BOT_TOKEN = "7704194972:AAFB_iOKXj2T2JKPbJUIPpSuczvT2mN_Lhw"  # Замените на свой токен

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Привет!  Я простой Telegram-бот.")

@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, f"Вы написали: {message.text}")

bot.polling()