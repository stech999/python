# Задача 16: Требуется вычислить, сколько раз встречается некоторое
# число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих
# строках записаны N целых чисел Ai
# . Последняя строка содержит число X
# 5
# 1 2 3 4 5
# 3
# -> 1
from array import *


num = int(input('Сколько элемнтов будет: '))
list1 = []
for i in range(num):
    b = int(input('Какую цифру записать: '))
    list1.append(b)
print("Наш новый список: ", list1)
print()
findnum = int(input('Какое число найти в списке: '))
count = 0
for i in range(len(list1)):
    if findnum == list1[i]:
        count += 1
print(f"Число {findnum} встречается {count} раз(а).")

# для самопроверки
# list_1 = [1, 2, 3, 4, 5]
# k = 3
# count = 0
# for i in range(len(list_1)):
#     if k == list_1[i]:
#         count += 1
# print(count)