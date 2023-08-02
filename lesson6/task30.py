# Задача 30: Заполните массив элементами арифметической
# прогрессии. Её первый элемент, разность и количество
# элементов нужно ввести с клавиатуры. Формула для
# получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.
# Ввод: 7 2 5
# Вывод: 7 9 11 13 15

def arr_arithmetic(first, diff, count):
    res = first
    for i in range(count - 1):
        res += diff
    return res




first_elem = int(input('Введите первый элемент: '))
difference = int(input('Разность элементов: '))
count_elem = int(input('количесто итоговых чисел: '))
print(f"Итог арифметической прогрессии: {arr_arithmetic(first_elem, difference, count_elem)}")