# Задача 20: В настольной игре Скрабл (Scrabble) каждая буква имеет определенную
# ценность. В случае с английским алфавитом очки распределяются так:
# ● A, E, I, O, U, L, N, S, T, R – 1 очко;
# ● D, G – 2 очка;
# ● B, C, M, P – 3 очка;
# ● F, H, V, W, Y – 4 очка;
# ● K – 5 очков;
# ● J, X – 8 очков;
# ● Q, Z – 10 очков.
# А русские буквы оцениваются так:
# ● А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# ● Д, К, Л, М, П, У – 2 очка;
# ● Б, Г, Ё, Ь, Я – 3 очка;
# ● Й, Ы – 4 очка;
# ● Ж, З, Х, Ц, Ч – 5 очков;
# ● Ш, Э, Ю – 8 очков;
# ● Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое содержит либо только
# английские, либо только русские буквы.
# Ввод:
# ноутбук
# Вывод:
# 12
# from array import *
#
# # english book
#
# k = "hello"
#
# sum = 0
# en10 = "A, E, I, O, U, L, N, S, T, R"
# en1 = en10.lower()
# points = int(1)
# en20 = "D, G"
# en2 = en20.lower()
# points2 = int(2)
# en30 = "B, C, M, P"
# en3 = en30.lower()
# points3 = int(3)
# en40 = "F, H, V, W, Y"
# en4 = en40.lower()
# points4 = int(4)
# en50 = "K"
# en5 = en50.lower()
# points5 = int(5)
# en60 = "J, X"
# en6 = en60.lower()
# points6 = int(8)
# en70 = "Q, Z"
# en7 = en70.lower()
# points7 = int(10)
#
# for i in range(len(en1)):
#     for j in range(len(k)):
#         if en1[i] == k[j]:
#             sum += points
#
# for i in range(len(en2)):
#     for j in range(len(k)):
#         if en2[i] == k[j]:
#             sum += points2
#
# for i in range(len(en3)):
#     for j in range(len(k)):
#         if en3[i] == k[j]:
#             sum += points3
#
# for i in range(len(en4)):
#     for j in range(len(k)):
#         if en4[i] == k[j]:
#             sum += points4
#
# for i in range(len(en5)):
#     for j in range(len(k)):
#         if en5[i] == k[j]:
#             sum += points5
#
# for i in range(len(en6)):
#     for j in range(len(k)):
#         if en6[i] == k[j]:
#             sum += points6
#
# for i in range(len(en7)):
#     for j in range(len(k)):
#         if en7[i] == k[j]:
#             sum += points7
#
# # russian book
#
# ru10 = "А, В, Е, И, Н, О, Р, С, Т"
# ru1 = ru10.lower()
# points11 = int(1)
# ru20 = "Д, К, Л, М, П, У"
# ru2 = ru20.lower()
# points22 = int(2)
# ru30 = "Б, Г, Ё, Ь, Я"
# ru3 = ru30.lower()
# points33 = int(3)
# ru40 = "Й, Ы"
# ru4 = ru40.lower()
# points44 = int(4)
# ru50 = "Ж, З, Х, Ц, Ч"
# ru5 = ru50.lower()
# points55 = int(5)
# ru60 = "Ш, Э, Ю"
# ru6 = ru60.lower()
# points66 = int(8)
# ru70 = "Ф, Щ, Ъ"
# ru7 = ru70.lower()
# points77 = int(10)
#
# for i in range(len(ru1)):
#     for j in range(len(k)):
#         if ru1[i] == k[j]:
#             sum += points11
#
# for i in range(len(ru2)):
#     for j in range(len(k)):
#         if ru2[i] == k[j]:
#             sum += points22
#
# for i in range(len(ru3)):
#     for j in range(len(k)):
#         if ru3[i] == k[j]:
#             sum += points33
#
# for i in range(len(ru4)):
#     for j in range(len(k)):
#         if ru4[i] == k[j]:
#             sum += points44
#
# for i in range(len(ru5)):
#     for j in range(len(k)):
#         if ru5[i] == k[j]:
#             sum += points55
#
# for i in range(len(ru6)):
#     for j in range(len(k)):
#         if ru6[i] == k[j]:
#             sum += points66
#
# for i in range(len(ru7)):
#     for j in range(len(k)):
#         if ru7[i] == k[j]:
#             sum += points77
#
#
# print(f"У слова '{k}' вышло {sum} очков(а).")







# --------------------- для самопроверки ---------------------





from array import *

# english book

k = "hello"

sum = 0
en10 = "A, E, I, O, U, L, N, S, T, R"
en1 = en10.lower()
points = int(1)
en20 = "D, G"
en2 = en20.lower()
points2 = int(2)
en30 = "B, C, M, P"
en3 = en30.lower()
points3 = int(3)
en40 = "F, H, V, W, Y"
en4 = en40.lower()
points4 = int(4)
en50 = "K"
en5 = en50.lower()
points5 = int(5)
en60 = "J, X"
en6 = en60.lower()
points6 = int(8)
en70 = "Q, Z"
en7 = en70.lower()
points7 = int(10)

for i in range(len(en1)):
    for j in range(len(k)):
        if en1[i] == k[j]:
            sum += points

for i in range(len(en2)):
    for j in range(len(k)):
        if en2[i] == k[j]:
            sum += points2

for i in range(len(en3)):
    for j in range(len(k)):
        if en3[i] == k[j]:
            sum += points3

for i in range(len(en4)):
    for j in range(len(k)):
        if en4[i] == k[j]:
            sum += points4

for i in range(len(en5)):
    for j in range(len(k)):
        if en5[i] == k[j]:
            sum += points5

for i in range(len(en6)):
    for j in range(len(k)):
        if en6[i] == k[j]:
            sum += points6

for i in range(len(en7)):
    for j in range(len(k)):
        if en7[i] == k[j]:
            sum += points7

# russian book

ru10 = "А, В, Е, И, Н, О, Р, С, Т"
ru1 = ru10.lower()
points11 = int(1)
ru20 = "Д, К, Л, М, П, У"
ru2 = ru20.lower()
points22 = int(2)
ru30 = "Б, Г, Ё, Ь, Я"
ru3 = ru30.lower()
points33 = int(3)
ru40 = "Й, Ы"
ru4 = ru40.lower()
points44 = int(4)
ru50 = "Ж, З, Х, Ц, Ч"
ru5 = ru50.lower()
points55 = int(5)
ru60 = "Ш, Э, Ю"
ru6 = ru60.lower()
points66 = int(8)
ru70 = "Ф, Щ, Ъ"
ru7 = ru70.lower()
points77 = int(10)

for i in range(len(ru1)):
    for j in range(len(k)):
        if ru1[i] == k[j]:
            sum += points11

for i in range(len(ru2)):
    for j in range(len(k)):
        if ru2[i] == k[j]:
            sum += points22

for i in range(len(ru3)):
    for j in range(len(k)):
        if ru3[i] == k[j]:
            sum += points33

for i in range(len(ru4)):
    for j in range(len(k)):
        if ru4[i] == k[j]:
            sum += points44

for i in range(len(ru5)):
    for j in range(len(k)):
        if ru5[i] == k[j]:
            sum += points55

for i in range(len(ru6)):
    for j in range(len(k)):
        if ru6[i] == k[j]:
            sum += points66

for i in range(len(ru7)):
    for j in range(len(k)):
        if ru7[i] == k[j]:
            sum += points77

print(sum)