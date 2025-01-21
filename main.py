import telebot

BOT_TOKEN = "7704194972:AAFB_iOKXj2T2JKPbJUIPpSuczvT2mN_Lhw"  # Замените на свой токен

bot = telebot.TeleBot(BOT_TOKEN)

# @bot.message_handler(commands= ['start', 'help'])
# def send_welcome(message):
#     bot.reply_to(message, "Привет!  Я простой Telegram-бот.")
#
# @bot.message_handler(func=lambda message: True)
# def echo_message(message):
#     bot.reply_to(message, f"Вы написали: {message.text}")

@bot.message_handler(commands=['start'])
def send_inline_keyboard(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    button1 = telebot.types.InlineKeyboardButton("Кнопка 1", callback_data="button1")
    button2 = telebot.types.InlineKeyboardButton("Кнопка 2", callback_data="button2")
    keyboard.add(button1, button2)
    bot.send_message(message.chat.id, "Выберите  кнопку:", reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def handle_callback(call):
    if call.data == "button1":
        bot.answer_callback_query(call.id, "Вы нажали кнопку 1!")
        bot.send_message(call.message.chat.id, "Вы выбрали кнопку 1")
    elif call.data == "button2":
        bot.answer_callback_query(call.id, "Вы нажали кнопку 2!")
        bot.send_message(call.message.chat.id, "Вы выбрали кнопку 2")

bot.polling()