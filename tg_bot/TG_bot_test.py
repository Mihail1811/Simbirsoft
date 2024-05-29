import telebot as tb
from telebot import types
import webbrowser, sqlite3
from aiogram import Bot, Dispatcher, types, executor

# ЧЕРЕЗ БИБЛИОТЕКУ TELEBOT
bot = tb.TeleBot('6706484283:AAH-A-rpXYitSHsTxgSohhryihBBhgmXOlA')

# команда /start
@bot.message_handler(commands=['start'])
def start(message):
# сообщение после ввода команды /start
    mess = f'Привет, <b><u>{message.from_user.first_name}</u></b>', 
    bot.send_message(message.chat.id, mess, parse_mode='html')

# ввод фотографии с ответом без пересылания
# @bot.message_handler(content_types=['photo'])
# def get_user_photo(message):
#     bot.send_message(message.chat.id, 'Вау, крутое фото!', parse_mode=['html'])

# ввод фотографии с ответом с пересыланием и добавлением кнопок
@bot.message_handler(content_types=['photo'])
def get_user_photo(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Перейти на сайт', url='https://google.com')
    btn2 = types.InlineKeyboardButton('Удалить фото', callback_data='delete')
    btn3 = types.InlineKeyboardButton('Изменить текст', callback_data='edit')
    markup.row(btn1)
    markup.row(btn2, btn3)
    bot.reply_to(message, 'Вау, крутое фото!', reply_markup=markup)


# обработка кнопок
@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == 'delete':
        bot.delete_message(callback.message.chat.id, callback.message.message_id - 1)
    elif callback.data == 'edit':
        bot.edit_message_text('Edit text', callback.message.chat.id, callback.message.message_id)


# Моментальный переход на сайт при введении команды /website
@bot.message_handler(commands=['website'])
def site(message):
    webbrowser.open('https://vk.com/id533035541')


# при вводе команды /site появляется две кнопки
@bot.message_handler(commands=['site'])
def website(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)

    website = types.KeyboardButton('как дела')
    start = types.KeyboardButton('что делаешь')

    markup.add(website, start)
    bot.send_message(message.chat.id, 'Нажми на любую кнопку!', reply_markup=markup)
    bot.register_next_step_handler(message, on_click)
# при нажатии на эти кнопки выводится текст
def on_click(message):
    if message.text == 'как дела':
        bot.send_message(message.chat.id, 'Все отлично')
    elif message.text == 'что делаешь':
        bot.send_message(message.chat.id, 'Отправляю тебе SMS')
    bot.register_next_step_handler(message, on_click)



# ввод любого текста
@bot.message_handler(content_types=['text'])
def get_user_text(message):
    if message.text.lower() == 'hello' or message.text.lower() == 'привет':
        bot.send_message(message.chat.id, 'И тебе привет!', parse_mode='html')
    elif message.text.lower() == 'id':
        bot.reply_to(message, f'Твой id: {message.from_user.id}', parse_mode='html')
    elif message.text == 'photo':
        photo = open('msg1041865190-130173.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)
    else:
        bot.send_message(message.chat.id, 'Я тебя не понимаю!', parse_mode='html')

# работа бота без остановки
bot.polling(none_stop=True)






# # ЧЕРЕЗ БИБЛИОТЕКУ AIOGRAM
bot = Bot('6706484283:AAH-A-rpXYitSHsTxgSohhryihBBhgmXOlA')
dp = Dispatcher(bot)

@dp.message_handler(commands=['inline'])
async def info(message: types.Message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('site', url = 'https://itproger.com'))
    markup.add(types.InlineKeyboardButton('Hello', callback_data='hello'))
    await message.reply('hello', reply_markup=markup)


@dp.callback_query_handler()
async def callback(call):
    await call.message.answer(call.data)


@dp.message_handler(commands=['reply'])
async def reply(message: types.Message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    markup.add(types.KeyboardButton('Website'))
    await message.answer('hello', reply_markup=markup)


@dp.message_handler(content_types=['text'])
async def start(message: types.Message):
    # await bot.send_message(message.chat.id, 'hello')
    # await message.answer('Hello')
    await message.reply('hello')
    # file = open('/some.png', 'rb')
    # await message.answer_photo(file)

executor.start_polling(dp)