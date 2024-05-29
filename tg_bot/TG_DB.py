import telebot as tb
from telebot import types
import webbrowser, sqlite3

bot = tb.TeleBot('6699744222:AAFL4OF93JBAdEl98a7q-xIHK36LjyFfTno')
name = None

# команда /start
@bot.message_handler(commands=['start'])
# подключение БД
def start(message):
    conn = sqlite3.connect('zhigan.sql')
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS users (id int auto_increment primary key, name varchar(50), pass varchar(50))')
    conn.commit()
    cur.close()
    conn.close()

# сообщение после ввода команды /start
    bot.send_message(message.chat.id, 'Привет, сейчас тебя зарегистрируем! Введите ваш никнейм')
    bot.register_next_step_handler(message, user_name)

# второе сообщение
def user_name(message):
    global name
    name = message.text.strip() 
    bot.send_message(message.chat.id, 'Введите пароль', parse_mode='html')
    bot.register_next_step_handler(message, user_pass)

# добавление пользователя в базу и вывод сообщения с кнопкой
def user_pass(message):
    password = message.text.strip() 

    conn = sqlite3.connect('zhigan.sql')
    cur = conn.cursor()
    cur.execute('INSERT INTO users (name, pass) VALUES ("%s", "%s")' % (name, password))
    conn.commit()
    cur.close()
    conn.close()

    markup = types.InlineKeyboardMarkup()
    markup.add(tb.types.InlineKeyboardButton('Список пользователей', callback_data='users'))
    bot.send_message(message.chat.id, 'Пользователь зарегистрирован!', reply_markup=markup)
    bot.register_next_step_handler(message, user_pass)


# обработка кнопок
@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    conn = sqlite3.connect('zhigan.sql')
    cur = conn.cursor()
    cur.execute('SELECT * FROM users')
    users = cur.fetchall()
    info = ''
    for el in users:
        info += f'Имя: {el[1]}, пароль: {el[2]}\n'
    cur.close()
    conn.close()

    bot.send_message(call.message.chat.id, info)

bot.polling(none_stop=True)