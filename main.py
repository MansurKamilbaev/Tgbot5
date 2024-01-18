# import telebot
# import webbrowser
#
# bot = telebot.TeleBot('6717597402:AAFWypDJJJHQ-9Yt1_O1xYY8H5dajbdkbwI')

#
# @bot.message_handler(commands=['site', 'website'])
# def site(message):
#     webbrowser.open('https://www.youtube.com/')
#
#
# @bot.message_handler()
# def info(message):
#     if message.text.lower() == 'привет':
#         bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}')
#
#     elif message.text.lower() == 'id':
#         bot.reply_to(message, f'ID: {message.from_user.id}')
#
#     elif message.text.lower() == '/start':
#         bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}')
#
#
# @bot.message_handler(commands=['start'])
# def start(message):
#     bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}')
#
#
# bot.infinity_polling()
