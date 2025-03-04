import telebot

BOT_TOKEN = "7636250407:AAF7YPi8sPk85jDARr41V2eI1VayVsKJS_o"
bot = telebot.TeleBot(BOT_TOKEN)

# База знаний
knowledge_base = {
    "minimalism": {
        "гостиная": {
            "цвет": {
                "белый": ["https://avatars.mds.yandex.net/i?id=c0cc9aac344ad2bac58495f411e56d30-5232511-images-thumbs&n=13"],
                "серый": ["https://avatars.mds.yandex.net/i?id=58604683860e676c438d8bcc448618d200ed6d795d358aff-12534005-images-thumbs&n=13"],
                "коричневый": ["https://avatars.mds.yandex.net/i?id=576d1fedebf6a6eb73141c9963165aac696c0d8f-10299502-images-thumbs&n=13"],
            }
        },
        "спальня": {
            "цвет": {
                "белый": ["https://avatars.mds.yandex.net/i?id=40be64df1c477c93a692f2bfd9a7fd39-3501814-images-thumbs&n=13"],
                "серый": ["https://avatars.mds.yandex.net/i?id=dfc1bbb329dc68491a8ddc3757e8be2f1558ce36-5606166-images-thumbs&n=13"],
                "коричневый": ["https://avatars.mds.yandex.net/i?id=4b43668b150d1a792cd23cccc75049a1220d2a21-4900921-images-thumbs&n=13"],
            }
        },
        "кухня": {
            "цвет": {
                "белый": ["https://avatars.mds.yandex.net/i?id=8f10ba24b7aa85b8ef2223f805ce9c3a5cbb8e11-10850090-images-thumbs&n=13"],
                "серый": ["https://avatars.mds.yandex.net/i?id=139dcf7758b8d68de7a4c0b7a2af56d07867ccf4-8282002-images-thumbs&n=13"],
                "коричневый": ["https://avatars.mds.yandex.net/i?id=52ccdb497cb6701fd0bf1ce41d2f59fd521631801d709878-12322312-images-thumbs&n=13"],
            }
        },
        "детская": {
            "цвет": {
                "белый": ["https://avatars.mds.yandex.net/i?id=aa9b9631892b975ef3658d209dbe7d648178dd29-8497900-images-thumbs&n=13"],
                "серый": ["https://avatars.mds.yandex.net/i?id=9a7aeaf8d80e689dce38e9b6060ce332-5875719-images-thumbs&n=13"],
                "коричневый": ["https://avatars.mds.yandex.net/i?id=fc1d6b3b4222f642c6d4f4a199eb91fa623ca106-10256664-images-thumbs&n=13"],
            }
        },
        "прихожая": {
            "цвет": {
                "белый": ["https://avatars.mds.yandex.net/i?id=800830123cb8c31cd8345075b913a92d1568baa5-10285533-images-thumbs&n=13"],
                "серый": ["https://avatars.mds.yandex.net/i?id=67e466ce22f2af369797e33adfd50cefd2b7415f-7051980-images-thumbs&n=13"],
                "коричневый": ["https://avatars.mds.yandex.net/i?id=30b3e5a0201c6b920635cce2a4ffb57d666200bd-10599899-images-thumbs&n=13"],
            }
        }
    },
},


user_data = {}

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    welcome_message = """
Привет! Я ваш помощник в дизайне интерьера. Вот что я могу:

/style - Выбрать стиль интерьера (например, /style minimalism)
"""
    bot.reply_to(message, welcome_message)


# Обработчик команды /style
@bot.message_handler(commands=['style'])
def ask_style(message):
    try:
        style_name = message.text.split(" ", 1)[1].lower()
        if style_name in knowledge_base:
            user_data[message.chat.id] = {"style": style_name, "step": "ask_room"}
            bot.reply_to(message, "Выберите тип помещения (гостиная, спальня, кухня, детская, прихожая):")
        else:
            bot.reply_to(message, "Извините, я не знаю такой стиль. Попробуйте ещё раз.")
    except IndexError:
        bot.reply_to(message, "Пожалуйста, укажите стиль после команды /style (например, /style minimalism)")


# Обработчик для выбора помещения
@bot.message_handler(func=lambda message: user_data.get(message.chat.id, {}).get("step") == "ask_room")
def ask_room(message):
    room = message.text.lower()
    if room in knowledge_base[user_data[message.chat.id]["style"]]:
        # Сохраняем выбранное помещение
        user_data[message.chat.id]["room"] = room
        user_data[message.chat.id]["step"] = "ask_color"
        # Спрашиваем цвет
        bot.reply_to(message, "Какой цвет вы предпочитаете? (например, белый, серый, коричневый)")
    else:
        bot.reply_to(message, "Пожалуйста, выберите одно из предложенных помещений (гостиная, спальня, кухня, детская, прихожая).")


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
