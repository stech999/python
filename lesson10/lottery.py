import telebot
from random import *
import time
from telebot import types

ticket = []
tic_win = []
ticket_coin = []

API_TOKEN='your token'
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def hel(message):
    keyboard_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_tomorrow = types.KeyboardButton('Играть')
    keyboard_markup.add(btn_tomorrow)
    bot.send_message(message.chat.id, f'Добро пожаловать на розыгрышь лотери.', reply_markup=keyboard_markup)

    # bot.send_message(message.chat.id, "Добро пожаловать на розыгрышь лотери.")
    bot.send_message(message.chat.id, "Чтобы выиграть в лотерее, надо иметь не только удачу, но и лотерейный билет.")
    bot.send_message(message.chat.id, "Призовой фонд 1 000 000$ \U0001F4B0 \n"
                                      "1 000$ - Если выпало 2 номера! \n"
                                      "10 000$ - Если выпало 3 номера! \n"
                                      "100 000$ - Если выпало 4 номера! \n"
                                      "1 000 000$ - Если выпало 5 номеров! \n")
    bot.send_message(message.chat.id, "Нажмите на кнопку | Играть | чтобы запустить лотерею!")


@bot.message_handler(content_types=['text'])
def bilet(message):
    if message.text == 'Играть':
        bot.send_message(message.chat.id, "Пожалуйста ждите, система генерирует вам номера.")
    random_digit()
    time.sleep(2)
    bot.send_message(message.chat.id, f"Вам выпали номера: {ticket}")
    bot.send_message(message.chat.id, "Формируется список выигрышных номеров, ожидайте ")
    t = 5
    while t > 0:
        bot.send_message(message.chat.id, t)
        t -= 1
        time.sleep(2)

    random_digit2()
    coincidence()
    bot.send_message(message.chat.id, f"Ваши номера: {ticket}")
    bot.send_message(message.chat.id, f"Выигрышные номера: {tic_win}")

    bot.send_message(message.chat.id, f"Совпал(и) номер(а/ов): {ticket_coin}") #среди ваших номеров выигрышных нет
    count = len(ticket_coin)
    if count == 1:
        bot.send_message(message.chat.id, "Удача улыбнется вам в следующий раз \U0001F62D")
        bot.send_message(message.chat.id, "Желаете сыграть еще раз? Тогда нажмите кнопку | Играть | внизу \U0001F603")
        ticket.clear()
        tic_win.clear()
    elif count == 2:
        bot.send_message(message.chat.id, "Вы выиграли! 1 000$ \U0001F4B0")
        bot.send_message(message.chat.id, "Желаете сыграть еще раз? Тогда нажмите кнопку | Играть | внизу \U0001F603")
        ticket.clear()
        tic_win.clear()
    elif count == 3:
        bot.send_message(message.chat.id, "Вы выиграли! 10 000$ \U0001F4B0")
        bot.send_message(message.chat.id, "Желаете сыграть еще раз? Тогда нажмите кнопку | Играть | внизу \U0001F603")
        ticket.clear()
        tic_win.clear()
    elif count == 4:
        bot.send_message(message.chat.id, "Вы выиграли! 100 000$ \U0001F4B0")
        bot.send_message(message.chat.id, "Желаете сыграть еще раз? Тогда нажмите кнопку | Играть | внизу \U0001F603")
        ticket.clear()
        tic_win.clear()
    elif count == 5:
        bot.send_message(message.chat.id, "Вы выиграли! 1 000 000$ \U0001F4B0")
        bot.send_message(message.chat.id, "Желаете сыграть еще раз? Тогда нажмите кнопку | Играть | внизу \U0001F603")
        ticket.clear()
        tic_win.clear()
    else:
        bot.send_message(message.chat.id, "Ошибка в системе! \U0001F632")
        ticket.clear()
        tic_win.clear()


def random_digit(): #создание уникальных номеров для пользователя
    while len(ticket) < 5:
        value = randint(1, 10)
        if value not in ticket:
            ticket.append(value)

def random_digit2(): #создание уникальных выигрышных номеров
    while len(tic_win) < 5:
        value = randint(1, 10)
        if value not in tic_win:
            tic_win.append(value)

def coincidence(): # модуль сравнение номеров
    for i in range(len(tic_win)):
        for j in range(len(ticket)):
            if tic_win[i] == ticket[j]:
                ticket_coin.append(tic_win[i])

bot.polling()