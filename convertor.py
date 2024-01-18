# import telebot
# from currency_converter import CurrencyConverter
# from telebot import types
#
# bot = telebot.TeleBot('6717597402:AAFWypDJJJHQ-9Yt1_O1xYY8H5dajbdkbwI')
# currency = CurrencyConverter()
# amount = 0
#
#
# @bot.message_handler(commands=['start'])
# def start(message):
#     bot.send_message(message.chat.id, 'Привет, введите сумму')
#     bot.register_next_step_handler(message, summ)
#
#
# def summ(message):
#     global amount
#     try:
#         amount = int(message.text.strip())
#     except ValueError:
#         bot.send_message(message.chat.id, 'Неверный формат. Впишите сумму')
#         bot.register_next_step_handler(message, summ)
#         return
#     if amount > 0:
#         markup = types.InlineKeyboardMarkup(row_width=2)
#         btn1 = types.InlineKeyboardButton('USD/EUR', callback_data='usd/eur')
#         btn2 = types.InlineKeyboardButton('EUR/USD', callback_data='eur/usd')
#         btn3 = types.InlineKeyboardButton('USD/RUB', callback_data='usd/rub')
#         btn4 = types.InlineKeyboardButton('Другое значение', callback_data='else')
#         markup.add(btn1, btn2, btn3, btn4)
#         bot.send_message(message.chat.id, 'Выберите пару валют', reply_markup=markup)
#     else:
#         bot.send_message(message.chat.id, 'Число должно быть больше за 0. Впишите сумму')
#         bot.register_next_step_handler(message, summ)
#
#
# @bot.callback_query_handler(func=lambda call: True)
# def callback(call):
#     if call.data != 'else':
#         values = call.data.upper().split('/')
#         res = currency.convert(amount, values[0], values[1])
#         bot.send_message(call.message.chat.id, f'Получается: {round(res, 2)}. Можете заново вписать сумму')
#         bot.register_next_step_handler(call.message, summ)
#     else:
#         bot.send_message(call.message.chat.id, 'Введите пару значений через слеш')
#         bot.register_next_step_handler(call.message, my_currency)
#
#
# def my_currency(message):
#     try:
#         values = message.upper().split('/')
#         res = currency.convert(amount, values[0], values[1])
#         bot.send_message(message.chat.id, f'Получается: {round(res, 2)}. Можете заново вписать сумму')
#         bot.register_next_step_handler(message, summ)
#     except Exception:
#         bot.send_message(message.chat.id, 'Что-то не так. Впишите значение заново')
#         bot.register_next_step_handler(message, my_currency)
#
#
#
#
# bot.infinity_polling()
