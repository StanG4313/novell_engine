import telebot
import os
from dotenv import load_dotenv
from telebot import types

load_dotenv()

API_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(func=lambda message: True)
def start(message):
    markup = types.InlineKeyboardMarkup()
    button = types.InlineKeyboardButton("Начнем!", callback_data='step2')
    markup.add(button)
    with open("./games/test_game/1.md", "r", encoding="utf-8") as file:
        with open("./games/test_game/1.jpeg", "rb") as photo:
            bot.send_photo(message.chat.id, photo)
        markdown_content = file.read()
        bot.send_message(message.chat.id, markdown_content, parse_mode="Markdown", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    markup = types.InlineKeyboardMarkup()
    if call.data == 'step2':
        with open("./games/test_game/2.md", "r", encoding="utf-8") as file:
            with open("./games/test_game/2.jpeg", "rb") as photo:
                bot.send_photo(call.message.chat.id, photo)
            markdown_content = file.read()
            button1 = types.InlineKeyboardButton("Опция 1", callback_data='step3.1')
            button2 = types.InlineKeyboardButton("Опция 2", callback_data='step3.2')
            markup.add(button1, button2)
            bot.send_message(call.message.chat.id, markdown_content, parse_mode="Markdown", reply_markup=markup)

    elif call.data == 'step3.1':
        with open("./games/test_game/3.1.md", "r", encoding="utf-8") as file:
            with open("./games/test_game/3.1.jpeg", "rb") as photo:
                bot.send_photo(call.message.chat.id, photo)
            markdown_content = file.read()
            button = types.InlineKeyboardButton("В конец", callback_data='step4')
            markup.add(button)
            bot.send_message(call.message.chat.id, markdown_content, parse_mode="Markdown", reply_markup=markup)

    elif call.data == 'step3.2':
        with open("./games/test_game/3.2.md", "r", encoding="utf-8") as file:
            with open("./games/test_game/3.2.jpeg", "rb") as photo:
                bot.send_photo(call.message.chat.id, photo)
            markdown_content = file.read()
            button = types.InlineKeyboardButton("В конец", callback_data='step4')
            markup.add(button)
            bot.send_message(call.message.chat.id, markdown_content, parse_mode="Markdown", reply_markup=markup)

    elif call.data == 'step4':
        with open("./games/test_game/4.md", "r", encoding="utf-8") as file:
            with open("./games/test_game/4.jpeg", "rb") as photo:
                bot.send_photo(call.message.chat.id, photo)
            markdown_content = file.read()
            bot.send_message(call.message.chat.id, markdown_content, parse_mode="Markdown", reply_markup=markup)


bot.polling()
