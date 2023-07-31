# дан некоторый список чисел, задача - найти сколько раз встречается введенная пользователем цифра
# например был список [1,15,55,7.58,0,99]
# и пользователь ввел 5
# ответ будет 4
# Это доп в рамках семинара.
# В ДЗ 3 семинара нет доп задачи . Только автотесты, только хардкор)
import math
from array import *
import string


num = "12.4"
output = num.translate(str.maketrans('', '', string.punctuation))
out = int(output)
x = int()
n = 1
count = 0
for i in range(len(output)):
    x = output[i]
    # if n == out[i]:
    #     count += 1
print(x)


# marks = ',.'
# num2 = []
# marks2 = '.'
# num3 = []
#
# for x in num:
#     if x in marks:
#         num2 = num.replace(x, "")
# for b in num2:
#     if b in marks2:
#         num3 = num.replace(b, "")
#
# print(num3, num2)