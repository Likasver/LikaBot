import telebot
from telebot import types

# Константы
BOT_TOKEN = "7636250407:AAGDTAep7JAP7Ak_h8Pq1Fih1kssm4-RJv4"
KNOWLEDGE_BASE = {
    "minimalism": {
        "гостиная": {
            "цвет": {
                "белый": ["https://example.com/white_living_room.jpg"],
                "серый": ["https://example.com/gray_living_room.jpg"],
                "коричневый": ["https://example.com/brown_living_room.jpg"],
            }
        },
        "спальня": {
            "цвет": {
                "белый": ["https://example.com/white_bedroom.jpg"],
                "серый": ["https://example.com/gray_bedroom.jpg"],
                "коричневый": ["https://example.com/brown_bedroom.jpg"],
            }
        },
        "кухня": {
            "цвет": {
                "белый": ["https://example.com/white_kitchen.jpg"],
                "серый": ["https://example.com/gray_kitchen.jpg"],
                "коричневый": ["https://example.com/brown_kitchen.jpg"],
            }
        },
        "детская": {
            "цвет": {
                "белый": ["https://example.com/white_kids_room.jpg"],
                "серый": ["https://example.com/gray_kids_room.jpg"],
                "коричневый": ["https://example.com/brown_kids_room.jpg"],
            }
        },
        "прихожая": {
            "цвет": {
                "белый": ["https://example.com/white_hallway.jpg"],
                "серый": ["https://example.com/gray_hallway.jpg"],
                "коричневый": ["https://example.com/brown_hallway.jpg"],
            }
        }
    }
}

# Инициализация бота
bot = telebot.TeleBot(BOT_TOKEN)

# Хранение данных пользователя
user_data = {}

# Команды
COMMANDS = {
    "start": "Начать работу с ботом",
    "help": "Получить справку по командам",
    "style": "Выбрать стиль интерьера (например, /style minimalism)",
}

# Сообщения
MESSAGES = {
    "welcome": """
Привет! Я ваш помощник в дизайне интерьера. Вот что я могу:
/style - Выбрать стиль интерьера (например, /style minimalism)
""",
    "unknown_command": "Извините, я не понимаю эту команду. Используйте /help для списка команд.",
    "style_not_found": "Извините, я не знаю такой стиль. Попробуйте ещё раз.",
    "room_not_found": "Пожалуйста, выберите одно из предложенных помещений (гостиная, спальня, кухня, детская, прихожая).",
    "color_not_found": "Извините, я не знаю такой цвет. Попробуйте ещё раз.",
    "photo_error": "Не удалось загрузить фото.",
}

# Обработчик команд /start и /help
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, MESSAGES["welcome"])

# Обработчик команды /style
@bot.message_handler(commands=['style'])
def ask_style(message):
    try:
        style_name = message.text.split(" ", 1)[1].lower()
        if style_name in KNOWLEDGE_BASE:
            user_data[message.chat.id] = {"style": style_name, "step": "ask_room"}
            bot.reply_to(message, "Выберите тип помещения (гостиная, спальня, кухня, детская, прихожая):")
        else:
            bot.reply_to(message, MESSAGES["style_not_found"])
    except IndexError:
        bot.reply_to(message, "Пожалуйста, укажите стиль после команды /style (например, /style minimalism)")

# Обработчик для выбора помещения
@bot.message_handler(func=lambda message: user_data.get(message.chat.id, {}).get("step") == "ask_room")
def ask_room(message):
    room = message.text.lower()
    if room in KNOWLEDGE_BASE[user_data[message.chat.id]["style"]]:
        user_data[message.chat.id]["room"] = room
        user_data[message.chat.id]["step"] = "ask_color"
        bot.reply_to(message, "Какой цвет вы предпочитаете? (например, белый, серый, коричневый)")
    else:
        bot.reply_to(message, MESSAGES["room_not_found"])

# Обработчик для выбора цвета
@bot.message_handler(func=lambda message: user_data.get(message.chat.id, {}).get("step") == "ask_color")
def ask_color(message):
    color = message.text.lower()
    style = user_data[message.chat.id]["style"]
    room = user_data[message.chat.id]["room"]

    if color in KNOWLEDGE_BASE[style][room]["цвет"]:
        user_data[message.chat.id]["color"] = color
        user_data[message.chat.id]["step"] = None

        photos = KNOWLEDGE_BASE[style][room]["цвет"][color]
        for photo_url in photos:
            try:
                bot.send_photo(message.chat.id, photo_url, caption=f"Пример стиля {style} для {room} в цвете {color}")
            except Exception as e:
                print(f"Ошибка отправки фото: {e}")
                bot.reply_to(message, MESSAGES["photo_error"])
    else:
        bot.reply_to(message, MESSAGES["color_not_found"])

    user_data.pop(message.chat.id, None)

# Обработчик для неизвестных команд
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, MESSAGES["unknown_command"])

# Запуск бота
if __name__ == "__main__":
    print("Бот запущен!")
    try:
        bot.infinity_polling()
    except Exception as e:
        print(f"Бот упал с ошибкой: {e}")