# # list   список      Змінний, Індексований, Ітерований
#
# # Змінний
#
# l = [1, 2, 3, 4, 5, 'Hello', True, 3.6, [1, 2, 3]]
#
# print(l)
# print(l[2])
# l[2] = 10
# print(l)
#
# # Індексований
# print(l[5])
# print()
# # Ітерований
# for elem in l:
#     print(elem)
#
# print('Hello' in l)
# print(l[8][2])
#
# l = [1, 2, 3, 4, 5, 'Hello', True, 3.6, 'Hello', [1, 2, 3]]
#
# # Кількість певних елементів в циклі
# l = [1, 2, 3, 4, 5, 'Hello', True, 3.6, 'Hello', [1, 2, 3]]
# word = 'Hello'
# count = 0
# for elem in l:
#     if word == elem:
#         count = count + 1
#         # count += 1
# print(f'Count of word {word} : {count}')
#
# # print(l[9][2])# Звертаємося до списоку в списку
#
# # Кількість певних елементів в циклі, навіть якщо вони є частиною елементу ~ 5 min
# l = [1, 2, 3, 4, 'Hello World!', 5, 'Hello', True, 'Hello World!!!111', 3.6, 'Hello', [1, 2, 3]]
# word = 'Hello'
# count = 0  # 4
# for elem in l:
#     if type(elem) == type('something') and word in elem:
#         print(type(elem))
#         count = count + 1
#         # count += 1
# print(f'Count of word {word} : {count}')
#
# print(type(1) == type(int()))
#
# word = 'Hello'
# count = l.count(word)
# print(f'Count of word {word} : {count}')
#
# # colors = list()
# colors = ['red', 'green', 'blue']
# print(colors)
# colors.append('purple')
# print(colors)
# colors.insert(1, 'orange')
# print(colors)
# print(colors.pop())
# print(colors.pop(1))
# print(colors)
#
# # tuple   кортеж      не змінний, Індексований, Ітерований
#
# t = (1, 2, 3, 4, 5, 'Hello', True, 3.6, [1, 2, 3])
# t = 1, 2, 3, 4, 5, 'Hello', True, 3.6, [1, 2, 3]
#
# l.append(123)
# print(l)
# t1 = tuple(l)
# print(t1)
#

