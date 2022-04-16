import telebot

TOKEN = '5180775199:AAEjTUYLxJ1as-YiuocKO5p81Da7lSLmZfw'
bot = telebot.TeleBot(f"{TOKEN}", parse_mode=False)
PASSW='1234'

main_buttons = ['Мои сессии', 'Мой аккаунт']

main_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)
for i in main_buttons:
    main_markup.add(i)

back_button = ['Вернуться в главное меню']
back_to_main_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
back_to_main_markup.add(back_button[0])

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет! Для того чтобы начать пользоваться, нужно авторизоваться!')
    process_enter(message)

def process_enter(message):
    msg = bot.send_message(message.chat.id, 'Введите ключ с сайта')
    bot.register_next_step_handler(msg, process_check)

def process_check(message):
    if message.text == PASSW:
        bot.send_message(message.chat.id, 'Отлично! Можешь начинать пользоваться.')
        main(message)
    else:
        bot.send_message(message.chat.id, 'Что-то пошло не так:( Попробуй еще раз')
        process_enter(message)

@bot.message_handler(func=lambda message: message.text==back_button[0])
def main(message):
    bot.send_message(message.chat.id, 'Вы в главном меню', reply_markup=main_markup)

@bot.message_handler(func=lambda message: message.text==main_buttons[1])
def my_account(message):
    text = f"{message.chat.first_name}\n\
Активных сессий: <получим>\n\
Закрытых сессий: <получим>"
    bot.send_message(message.chat.id, text, reply_markup=back_to_main_markup)

bot.infinity_polling()