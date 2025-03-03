import telebot

BOT_TOKEN = "7636250407:AAFcKjZor6MKo4rBgJyD-qAkTBV1czU3Cmw"
bot = telebot.TeleBot(BOT_TOKEN)

# База знаний
knowledge_base = {
    "minimal": {
        "гостиная": {
            "цвет": {
                "белый": ["https://img.lu.ru/add_photo/big/m/a/x/maxisvet_1_1685_20_cr_led_y_g4_4.jpg"],
                "серый": ["https://example.com/grey_living_room.jpg"]  # Замените на реальный URL
            }
        },
        "спальня": {
            "цвет": {
                "белый": ["https://example.com/white_bedroom.jpg"],  # Замените на реальный URL
                "серый": ["https://example.com/grey_bedroom.jpg"]  # Замените на реальный URL
            }
        }
    },
    "loft": {
        "гостиная": {
            "цвет": {
                "белый": ["https://img.lu.ru/add_photo/big/m/a/x/maxisvet_1_1685_20_cr_led_y_g4_4.jpg"],
                "серый": ["https://example.com/grey_living_room.jpg"]  # Замените на реальный URL
            }
        },
        "спальня": {
            "цвет": {
                "белый": ["https://example.com/white_bedroom.jpg"],  # Замените на реальный URL
                "серый": ["https://example.com/grey_bedroom.jpg"]  # Замените на реальный URL
            }
        }
    }
}

# Словарь для хранения состояний пользователей
user_data = {}


# Обработчик команд /start и /help
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    welcome_message = """
Привет! Я ваш помощник в дизайне интерьера. Вот что я могу:

/style - Выбрать стиль интерьера (например, /style minimal)
"""
    bot.reply_to(message, welcome_message)


# Обработчик команды /style
@bot.message_handler(commands=['style'])
def ask_style(message):
    try:
        style_name = message.text.split(" ", 1)[1].lower()  # Получаем название стиля
        if style_name in knowledge_base:
            # Сохраняем выбранный стиль для пользователя
            user_data[message.chat.id] = {"style": style_name, "step": "ask_room"}
            # Спрашиваем тип помещения
            bot.reply_to(message, "Выберите тип помещения (гостиная, спальня):")
        else:
            bot.reply_to(message, "Извините, я не знаю такой стиль. Попробуйте ещё раз.")
    except IndexError:
        bot.reply_to(message, "Пожалуйста, укажите стиль после команды /style (например, /style minimal)")


# Обработчик для выбора помещения
@bot.message_handler(func=lambda message: user_data.get(message.chat.id, {}).get("step") == "ask_room")
def ask_room(message):
    room = message.text.lower()
    if room in knowledge_base[user_data[message.chat.id]["style"]]:
        # Сохраняем выбранное помещение
        user_data[message.chat.id]["room"] = room
        user_data[message.chat.id]["step"] = "ask_color"
        # Спрашиваем цвет
        bot.reply_to(message, "Какой цвет вы предпочитаете? (например, белый, серый)")
    else:
        bot.reply_to(message, "Пожалуйста, выберите одно из предложенных помещений (гостиная, спальня).")


# Обработчик для выбора цвета
@bot.message_handler(func=lambda message: user_data.get(message.chat.id, {}).get("step") == "ask_color")
def ask_color(message):
    color = message.text.lower()
    style = user_data[message.chat.id]["style"]
    room = user_data[message.chat.id]["room"]

    # Проверяем, есть ли такой цвет для выбранного стиля и помещения
    if color in knowledge_base[style][room]["цвет"]:
        # Сохраняем выбранный цвет
        user_data[message.chat.id]["color"] = color
        user_data[message.chat.id]["step"] = None  # Завершаем цепочку вопросов

        # Получаем фотографии для выбранного цвета
        photos = knowledge_base[style][room]["цвет"][color]

        # Отправляем фотографии
        for photo_url in photos:
            try:
                bot.send_photo(message.chat.id, photo_url, caption=f"Пример стиля {style} для {room} в цвете {color}")
            except Exception as e:
                print(f"Ошибка отправки фото: {e}")
                bot.reply_to(message, f"Не удалось загрузить фото с URL: {photo_url}.")
    else:
        bot.reply_to(message, "Извините, я не знаю такой цвет. Попробуйте ещё раз.")

    # Очищаем данные пользователя
    user_data.pop(message.chat.id, None)


# Обработчик для неизвестных команд
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "Извините, я не понимаю эту команду. Используйте /help для списка команд.")


# Запуск бота
if __name__ == "__main__":
    print("Бот запущен!")
    try:
        bot.infinity_polling()
    except Exception as e:
        print(f"Бот упал с ошибкой: {e}")
