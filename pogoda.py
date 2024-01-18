# import telebot
# import requests
# import json
#
# bot = telebot.TeleBot('6717597402:AAFWypDJJJHQ-9Yt1_O1xYY8H5dajbdkbwI')
# API = '78c00512ffb81d138289b7d8122a5296'
#
#
# @bot.message_handler(commands=['start'])
# def start(message):
#     bot.send_message(message.chat.id, 'Привет, рад тебя видеть! Напиши название города')
#
#
# @bot.message_handler(content_types=['text'])
# def get_weather(message):
#     city = message.text.strip().lower()
#     res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
#     if res.status_code == 200:
#         data = json.loads(res.text)
#         temp = data['main']['temp']
#         bot.reply_to(message, f'Сейчас погода: {data["main"]["temp"]}')
#
#         image = 'sun.webp' if temp > 5.0 else 'i.webp'
#         file = open('./' + image, 'rb')
#         bot.send_photo(message.chat.id, file)
#
#     else:
#         bot.reply_to(message, 'Город указан не верно')
#
#
# bot.infinity_polling()
