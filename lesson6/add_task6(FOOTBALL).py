# Задача FOOTBALL необязательная
# Напишите программу, которая принимает на стандартный вход список игр футбольных команд
# с результатом матча и выводит на стандартный вывод сводную таблицу результатов всех матчей.
# За победу команде начисляется - 3 очка, за поражение - 0, за ничью - 1.
#
# Формат ввода следующий:
# В первой строке указано целое число nn — количество завершенных игр.
# После этого идет nn строк, в которых записаны результаты игры в следующем формате:
# Перваякоманда; Забитопервойкомандой; Втораякоманда; Забитовторойкомандой
#
# Вывод программы необходимо оформить следующим образом:
# Команда:Всегоигр Побед Ничьих Поражений Всего очков
#
# Конкретный пример ввода-вывода приведён ниже.
# Порядок вывода команд произвольный.
# Пример входа: 3
# Спартак;9 ;Зенит;10
# Локомотив;12 ;Зенит;3
# Спартак;8; Локомотив;15
# Выход будет:
# Спартак:2 0 0 2 0
# Зенит:2 1 0 1 3
# Локомотив:2 2 0 0 6
# 1 - Зенит
# 2 - Спартак
# 3 - Локомотив
from random import randint

def rand_points(points):
    sp = [randint(0, 2) for _ in range(points)]
    return sp
def resultat_lost(score):
    sp = 0
    for i in range(len(score)):
        if score[i] == 0:
            sp += 1
    return sp
def resultat_draw(score):
    sp = 0
    for i in range(len(score)):
        if score[i] == 1:
            sp += 1
    return sp
def resultat_win(score):
    sp = 0
    for i in range(len(score)):
        if score[i] == 2:
            sp += 1
    return sp
def score_points(points):
    sp = 0
    for i in range(len(points)):
        if points[i] == 1:
            sp += 1
        if points[i] == 2:
            sp += 3
    return sp




score_com = int(input('Сколько игр сыграла каждая команда: '))
com1 = rand_points(score_com)
com2 = rand_points(score_com)
com3 = rand_points(score_com)
print(f'Зенит - {com1} \nСпартак - {com2} \nЛокомотив - {com3}')
print(f"Команда Зенит сыграла всего {score_com} игр из них:\nПроиграла {resultat_lost(com1)} игр(ы/у)\nНичья {resultat_draw(com1)} игр(ы/у)\nВыиграла {resultat_win(com1)} игр(ы/у)")
print()
print(f"Команда Спартак сыграла всего {score_com} игр из них:\nПроиграла {resultat_lost(com2)} игр(ы/у)\nНичья {resultat_draw(com2)} игр(ы/у)\nВыиграла {resultat_win(com2)} игр(ы/у)")
print()
print(f"Команда Локомотив сыграла всего {score_com} игр из них:\nПроиграла {resultat_lost(com3)} игр(ы/у)\nНичья {resultat_draw(com3)} игр(ы/у)\nВыиграла {resultat_win(com3)} игр(ы/у)")
print()
print("Каждая команда набрала:")
print(f"Зенит - {score_points(com1)} очко(а/в)")
print(f"Спартак - {score_points(com2)} очко(а/в)")
print(f"Локомотив - {score_points(com3)} очко(а/в)")
