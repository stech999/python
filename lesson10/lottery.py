import telebot
from random import *
import time
from telebot import types
import html

ticket = []
tic_win = []
ticket_coin = []

API_TOKEN = 'token'
bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    keyboard_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_play = types.KeyboardButton('Играть')
    btn_info = types.KeyboardButton('Информация о выигрыше')
    keyboard_markup.add(btn_play, btn_info)
    bot.send_message(message.chat.id, f'Добро пожаловать на розыгрышь лотери.', reply_markup=keyboard_markup)
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
        time.sleep(2)
        t = 5
        while t > 0:
            bot.send_message(message.chat.id, t)
            t -= 1
            time.sleep(2)

        random_digit2()
        coincidence()
        bot.send_message(message.chat.id, f"Ваши номера: {ticket}")
        time.sleep(2)
        bot.send_message(message.chat.id, f"Выигрышные номера: {tic_win}")
        time.sleep(2)

        count = len(ticket_coin)
        if count == 0:
            bot.send_message(message.chat.id, f"Среди ваших номеров выигрышных нет \U0001F626")
            bot.send_message(message.chat.id, "Желаете сыграть еще раз? Тогда нажмите кнопку | Играть | \U0001F603")
            ticket.clear()
            tic_win.clear()
            ticket_coin.clear()
        elif count == 1:
            bot.send_message(message.chat.id, f"Совпало всего 1 номер \U0001F626 {ticket_coin}")
            bot.send_message(message.chat.id, "Удача улыбнется вам в следующий раз \U0001F62D")
            bot.send_message(message.chat.id, "Желаете сыграть еще раз? Тогда нажмите кнопку | Играть | \U0001F603")
            ticket.clear()
            tic_win.clear()
            ticket_coin.clear()
        elif count == 2:
            bot.send_message(message.chat.id, f"Совпало 2 номера: {ticket_coin}")
            bot.send_message(message.chat.id, "Вы выиграли! 1 000$ \U0001F4B0")
            bot.send_message(message.chat.id, "Желаете сыграть еще раз? Тогда нажмите кнопку | Играть | \U0001F603")
            ticket.clear()
            tic_win.clear()
            ticket_coin.clear()
        elif count == 3:
            bot.send_message(message.chat.id, f"Совпало 3 номера: {ticket_coin}")
            bot.send_message(message.chat.id, "Вы выиграли! 10 000$ \U0001F4B0")
            bot.send_message(message.chat.id, "Желаете сыграть еще раз? Тогда нажмите кнопку | Играть | \U0001F603")
            ticket.clear()
            tic_win.clear()
            ticket_coin.clear()
        elif count == 4:
            bot.send_message(message.chat.id, f"Совпало 4 номера: {ticket_coin}")
            bot.send_message(message.chat.id, "Вы выиграли! 100 000$ \U0001F4B0")
            bot.send_message(message.chat.id, "Желаете сыграть еще раз? Тогда нажмите кнопку | Играть | \U0001F603")
            ticket.clear()
            tic_win.clear()
            ticket_coin.clear()
        elif count == 5:
            bot.send_message(message.chat.id, f"Совпало 5 номеров: {ticket_coin}")
            bot.send_message(message.chat.id, "Вы везунчик, Вы выиграли! 1 000 000$ \U0001F4B0")
            bot.send_message(message.chat.id, "Желаете сыграть еще раз? Тогда нажмите кнопку | Играть | \U0001F603")
            ticket.clear()
            tic_win.clear()
            ticket_coin.clear()
    elif message.text == 'Информация о выигрыше':
        bot.send_message(message.chat.id, "Призовой фонд 1 000 000$ \U0001F4B0 \n"
                                          "1 000$ - Если выпало 2 номера! \n"
                                          "10 000$ - Если выпало 3 номера! \n"
                                          "100 000$ - Если выпало 4 номера! \n"
                                          "1 000 000$ - Если выпало 5 номеров! \n")

    else:
        bot.send_message(message.chat.id, "Ошибка в системе! \U0001F632")
        ticket.clear()
        tic_win.clear()
        ticket_coin.clear()


def random_digit():  # создание уникальных номеров для пользователя
    while len(ticket) < 5:
        value = randint(1, 10)
        if value not in ticket:
            ticket.append(value)


def random_digit2():  # создание уникальных выигрышных номеров
    while len(tic_win) < 5:
        value = randint(1, 10)
        if value not in tic_win:
            tic_win.append(value)


def coincidence():  # модуль сравнение номеров
    for i in range(len(tic_win)):
        for j in range(len(ticket)):
            if tic_win[i] == ticket[j]:
                ticket_coin.append(tic_win[i])


bot.polling()