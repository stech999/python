# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы
# расплачивались за проезд и получали билет с номером. Счастливым
# билетом называют такой билет с шестизначным номером, где сумма
# первых трех цифр равна сумме последних трех. Т.е. билет с номером
# 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать
# программу, которая проверяет счастливость билета.
# 385916 -> yes
# 123456 -> no

n = 385916
n_str = str(n)
n1 = n_str[:len(n_str)//2]
n2 = n_str[len(n_str)//2:]

n_int = int(n1)
a = 0
b = 0
i = 0
while i < len(n1):
    a = n_int % 10
    b += a
    n_int //= 10
    i += 1
# print(b)

n_int2 = int(n2)
a1 = 0
b1 = 0
j = 0
while j < len(n2):
    a1 = n_int2 % 10
    b1 += a1
    n_int2 //= 10
    j += 1
# print(b1)

if b == b1:
    print("yes")
else:
    print("no")