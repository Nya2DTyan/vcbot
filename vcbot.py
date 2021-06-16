import telebot
from telebot import types

token = "1709546579:AAGSRSy4hDPw-fGsvjFn45OoRIbKYyGquDM"
bot = telebot.TeleBot(token, parse_mode=None)

buttons_text = ['Тарифы','Просчет','Регистрация','Инфо']

@bot.message_handler(commands = ['start'])
def StartWithKB(message):
  markup = types.ReplyKeyboardMarkup(row_width = 2)
  buttons = [types.KeyboardButton(btn_text) for btn_text in buttons_text]
  markup.add(*buttons)
  bot.send_message(message.chat.id,'''Привет, я бот, который имеет слудущие функции:
  - При нажатии на кнопку [ТАРИФЫ] вы сможете увидеть наши цены на услуги.
  - При нажатии на кнопку [ПРОСЧЕТ] вы сможете есплатно просчитать свои...
  - При нажатии на кнопку [РЕГИСТРАЦИЯ] вы сможете стать нашим книентом по инструкции, которая появится при нажатии на кнопку.
  - При нажатии на кнопку [ИНФО] вы сможете ужать дополнительную информацию.''',reply_markup = markup)

@bot.message_handler()
def answer(message):
  if (message.text == 'Тарифы'):
    bot.send_message(message.chat.id, '''Наши цены:
    Жд - ... 
    Морем - ...
    Авиа - ...
    Бренд - ... 
    
    Ссылка на изменяемый файл: https://docs.google.com/document/d/1e_CYdZ5ybPCopT0BlZVtZTzFmCfYWO_MfYx0B-QSD_E/edit?usp=sharing ''')

  elif (message.text == 'Просчет'):
    bot.send_message(message.chat.id, 'Тут типо должен быть просчет')

  elif (message.text == 'Регистрация'):
    bot.send_message(message.chat.id, '''Для того, что бы стать нашим клиентом, отправьте в этот чат сообщение за примером, менеджер его обработает и... 
    1) ФИО
    2) Ел.почта
    3) Тип отправки
    4)...''')

  elif (message.text == 'Инфо'):
    markup_inline = types.InlineKeyboardMarkup(row_width=1)
    item_1 = types.InlineKeyboardButton(text = 'Условия работы', callback_data = 'Условия работы')
    item_2 = types.InlineKeyboardButton(text = 'Как мы работаем?', callback_data = 'Как мы работаем?')
    item_3 = types.InlineKeyboardButton(text = 'Адреса складов', callback_data = 'Адреса складов')
    item_4 = types.InlineKeyboardButton(text = 'Бланк заказов', callback_data = 'Бланк заказов')

    markup_inline.add(item_1, item_2, item_3, item_4)
    bot.send_message(message.chat.id,'''Ниже предоставлены кнопки, нажав на которые вы можете узнат интересующую вас информацию.''', reply_markup = markup_inline)

  else:
    pass

@bot.callback_query_handler(func = lambda call: True)
def answerForKB(call, message):
  if call.data == 'Условия Работы':
    bot.send_message(message.chat.id, 'Тут что-то нужно придумать')

  elif call.data == 'Как мы работаем?':
    bot.send_message(message.chat.id, 'И тут что-то нужно придумать')

  elif call.data == 'Адреса складов':
    bot.send_message(message.chat.id, 'Тут какой-то адрес')
    
  elif call.data == 'Бланк заказов':
    bot.send_message(message.chat.id, 'нужно какой-то файл скидывать')

bot.polling()