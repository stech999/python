# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного
# максимума)
# Ввод: [-5, 9, 0, 3, -1, -2, 1,
# 4, -2, 10, 2, 0, -9, 8, 10, -9,
# 0, -5, -5, 7]
# Вывод: [1, 9, 13, 14, 19]
from random import randint

def first_sp(count_el, f_el, sec_el):
    spisok = [randint(f_el, sec_el) for _ in range(count_el)]
    return spisok
def ind_elem(init1, end1, red_sp):
    print('Готовый список индексов в диапозоне элементов: ')
    for i in range(len(red_sp)):
        if red_sp[i] > init1 and red_sp[i] < end1:
            # sp.append(i)
            print(i, " = ", red_sp[i], end = " | ")




count_el = int(input('Количество элементов для вывода: '))
f_element = int(input('Начальная цифра для диапозона элементов, например: -50: '))
sec_element = int(input('Последняя цфира для диапозона элементов, например: 70: '))
ready_sp = first_sp(count_el, f_element, sec_element)
print(f"Первоначальный список: {ready_sp}")

print("Поиск индексов в диапозоне цифр:")
init_num = int(input('Начальный элемент: '))
end_num = int(input('Последний элемент: '))
ind_elem(init_num, end_num, ready_sp)