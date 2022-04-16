import telebot
from db import *


class User:
    def __init__(self, name, chat_id):
        self.name = name
        self.chat_id = chat_id
        self.key = None
        self.sessions = []

    def update_sessions(self):
        self.sessions = [Session('Сессия 1'), Session('Сессия 2'), Session('Сессия 3')] #будем получать сессии


class Session:
    def __init__(self, name):
        self.name = name
        self.rate = 20 # надо будет изменить конструктор, когда будет готово, откуда получать
        self.is_min_rate=False
        self.is_auto_mode = False



    def update_rate(self):
        self.rate = 15 #подключаюсь


TOKEN = '5180775199:AAEjTUYLxJ1as-YiuocKO5p81Da7lSLmZfw'
bot = telebot.TeleBot(f"{TOKEN}", parse_mode=False)
PASSW='1234'

main_buttons = ['Мои сессии', 'Мой аккаунт']
sessions_buttons = ['Активные сессии', 'История сессий']
back_buttons = ['Вернуться назад']

users = {}
engine = create_engine('sqlite:///:memory:', echo=True)



main_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)
for i in main_buttons:
    main_markup.add(i)

back_to_main_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
back_to_main_markup.add(back_buttons[0])

session_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)
session_markup.add(*sessions_buttons)
session_markup.add(*back_buttons)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет! Для того чтобы начать пользоваться, нужно авторизоваться!')
    process_enter(message)

def process_enter(message):
    msg = bot.send_message(message.chat.id, 'Введите ключ с сайта')
    bot.register_next_step_handler(msg, process_check)

def process_check(message):
    if message.text == PASSW:
        users[message.chat.id] = User(message.chat.id ,message.chat.first_name)
        bot.send_message(message.chat.id, 'Отлично! Можешь начинать пользоваться.')
        main(message)
    else:
        bot.send_message(message.chat.id, 'Что-то пошло не так:( Попробуй еще раз')
        process_enter(message)

@bot.message_handler(func=lambda message: message.text==back_buttons[0])
def main(message):
    bot.send_message(message.chat.id, 'Вы в главном меню', reply_markup=main_markup)

@bot.message_handler(func=lambda message: message.text==main_buttons[1])
def my_account(message):
    text = f"{message.chat.first_name}\n\
Активных сессий: <получим>\n\
Закрытых сессий: <получим>"
    bot.send_message(message.chat.id, text, reply_markup=back_to_main_markup)


@bot.message_handler(func=lambda message: message.text==main_buttons[0])
def my_sessions(message):
    bot.send_message(message.chat.id, 'Выберите действие', reply_markup=session_markup)

@bot.message_handler(func=lambda message: message.text==sessions_buttons[0])
def active_sessions(message):
    id = message.chat.id
    users[id].update_sessions() # обновим сессии
    markup = telebot.types.InlineKeyboardMarkup()
    buttons = []
    for i in range(len(users[id].sessions)):
        buttons.append(
            telebot.types.InlineKeyboardButton(users[id].sessions[i].name, callback_data=str(i))
        )
    for button in buttons:
        markup.add(button)
    bot.send_message(id, 'Выбирайте сессию', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data.isdigit())
def active_sessions_buttons(call):
    sessions = users[call.message.chat.id].sessions
    for i in range(len(sessions)):
        if call.data==str(i):
            markup = telebot.types.InlineKeyboardMarkup()
            buttons = []
            buttons.append(telebot.types.InlineKeyboardButton('Понизить ставку(вручную)', callback_data='handle'))
            buttons.append(telebot.types.InlineKeyboardButton('Указать минимальную цену заказа', callback_data='auto'))
            markup.add(*buttons)
            bot.edit_message_text(#получаем инфу
text=f"Котировочная сессия {sessions[i].name}\n\
Ваша ставка ставка последняя в котировке>\n\
<Минимальная сумма, с которой прекращается бот>\n\
<Текущая ставка>{sessions[i].rate}",
chat_id=call.message.chat.id,
message_id=call.message.message_id,
reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def string_callback_data(call):
    if call.data == 'handle':
        msg = bot.send_message(call.message.chat.id, 'Введите сумму, которая будет в итоге', reply_markup=back_to_main_markup)
        bot.register_next_step_handler(msg, process_change_min)
    elif call.data == 'auto':
        bot.send_message(call.message.chat.id, 'Прогнозирующий режим включен!')
        active_sessions(call.message)
        #передаю артему изменение режима
def process_change_min(message):
    print(message.text)
    #####Посылаю Артему обноление мин суммы и ставлю режим
    active_sessions(message)


bot.infinity_polling()