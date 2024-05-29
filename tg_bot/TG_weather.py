import telebot as tb
import requests
import json

bot = tb.TeleBot('6847774584:AAG8IPBo2sM6cj69gnyMiDykuRFPVyOh6m8')
API = 'c917940a8fae95c6fb7a35dbd6f07674'

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет, рад тебя видеть! Напиши название города')


@bot.message_handler(content_types=['text'])
def det_wether(message):
    city = message.text.strip().lower()
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
    if res.status_code == 200:
        data = json.loads(res.text)
        temp = data['main']['temp']
        bot.reply_to(message, f'Сейчас погода: {data["main"]["temp"]}')

        image = 'img/sunnyj.png' if temp > 5.0 else 'img/bad.png'
        file = open('./' + image, 'rb')
        bot.send_photo(message.chat.id, file)
    else:
        bot.reply_to(message, "Город указан не верно!")

bot.polling(none_stop=True)