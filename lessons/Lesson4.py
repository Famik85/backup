# s = "Hello World!"  # str
# print(s)
#
# print(s[0], s[1], s[2], s[3])
#
# s = "Hello World!"
# #    0123456789
#
# #   Незмінний, індексований, ітерований тип данних
#
#
# # Незмінний
# s = 'Hello'
# s = s + ' World!'
#
# # індексований
# print(s[0], s[1], s[2], s[3])
#
# # ітерований
# s = "Hello World!"
# for elem in s:
#     print(elem)
#
# n = 'Andrii Builuk'
# #    0123456789
# print(n[7], n[8], n[9], n[10], n[2])  # B u i l d
# print(n[2], n[3], n[4], n[10], n[10])  # d r i l l
# print(n[2], n[3], n[4], n[1], n[12])  # d r i n k
#
# n = "Serhii Cherniaiev"
# #    0123456789
# print(n[3], n[4])  # hi
#
# name = "Anatolii Kostiuk"
# print(name[9], name[10], name[11], name[0])
# print(name[9], name[10], name[11], name[12], name[13])
# print(name[0], name[9], name[11])
# # Atoll
#
# n = "Alexandr Reva"
#
# print(n[7], n[2], n[11], n[2], n[0], n[1], )  # Раскрывать
# print(n[7], n[4], n[11], n[2], n[5])  # Ворон
# print(n[2], n[1], n[2], n[11], n[2], n[5])  # Одиннадцать
#
# s = "Hello World!"
# #    0123456789
#
# print(s[0:5])  # Hello
# print(s[6:11])  # World
#
# print(s[:5])  # Hello
# print(s[6:])  # World!
# print(s[::-1])  # !dlroW olleH
#
# new_word = s[6:9] + s[10]
# print(new_word)
#
# s = "John's"
# print(s)
# s = 'John"s'
# print(s)
#
# print("John's John\"s")
#
# print('Hello ' * 5)
#
# s = "Hello World!"
# print(len(s))
#
# s = "Hello World!"
# count = 0
# letter = "l"
#
# for elem in s:
#     if elem == letter:
#         count = count + 1
#
# print(count)
#
# s = "Hello World!"
# count = 0
# letter = "l"
#
# print(s.count(letter))
#
# text = 'asdfg12345'
# # Користувач пише текст, підрахуват кількість в ньому літер і цифр і вивести.
# # 1.1
# digit_count = 0
# letter_count = 0
# for elem in text:
#     if elem == '0':
#         digit_count = digit_count + 1
#     elif elem == '1':
#         digit_count = digit_count + 1
#
# # 1.2
# digit_count = 0
# letter_count = 0
# for elem in text:
#     if elem == '0' or elem == '1' or elem == '2':
#         digit_count = digit_count + 1
#     elif elem == 'a' or elem == 'b':
#         letter_count = letter_count + 1
#
# # 2
# digits = '0123456789'
# letters = 'abcdefghijklmnopqrstuvwxyz'
# digit_count = 0
# letter_count = 0
# for elem in text:
#     if elem in digits:
#         digit_count = digit_count + 1
#     elif elem in letters:
#         letter_count = letter_count + 1
# print(f'Digits: {digit_count}, Letters: {letter_count}')
# # 3
# digit_count = 0
# letter_count = 0
# for elem in text:
#     if elem.isdigit():
#         digit_count = digit_count + 1
#     elif elem.isalpha():
#         letter_count = letter_count + 1
# print(f'Digits: {digit_count}, Letters: {letter_count}')
#
# e = 'é'
# print(e.isalpha())
#
# s = "Hello World!"
# print(s.find('l'))#2
# print(s.rfind('l'))#9
#
# s = "Hello World!"
# #-      987654321
#
# s = "hello world"
# print(s.islower())#True
# print(s.upper())#HELLO WORLD
#
# #ПриватБанк
# #приват пріват ПРИВАТБАНК
#
# text = '''French orthography encompasses the spelling and punctuation of the French language. It is based on a combination of phonemic and historical principles. The spelling of words is largely based on the pronunciation of Old French c. 1100–1200 AD, and has stayed more or less the same since then, despite enormous changes to the pronunciation of the language in the intervening years. Even in the late 17th century, with the publication of the first French dictionary by the Académie française, there were attempts to reform French orthography.'''
# print(text)
# print(text.replace('French','English'))
#
# #* Зробити программу, яка емулює метод replace
#
# password = 'Qa1Kl3!&'
# digit = False
# low_alpha = False
# up_alpha = False
# symbol = False
# length = 0
# for elem in password:
#     if elem.isdigit():
#         digit = elem.isdigit()
#     elif elem.islower():
#         low_alpha = elem.islower()
#     elif elem.isupper():
#         up_alpha = elem.isupper()
#     elif elem in '!@#$%^&*':
#         symbol = True
#     length = length + 1
#
# if length >= 8 and symbol and up_alpha and low_alpha and digit:
#     print('Very strong password!')
# elif length >= 8 and up_alpha and low_alpha and digit:
#     print('Strong password!')
# elif length >= 8 and (up_alpha or low_alpha) and digit:
#     print('Normal password!')
# elif length >= 8 and (up_alpha or low_alpha or digit):
#     print('Easy password!')
#
# else:
#     print('Bad password')

while True:
    number1 = ''
    command = ''
    number2 = ''
    result = ''
    while not number1.isdigit():
        number1 = str(input("Enter number1: "))

    number1 = int(number1)

    while command != '+' and command != '-':
        command = str(input("Enter command: "))

    while not number2.isdigit():
        number2 = str(input("Enter number2: "))

    number2 = int(number2)
    if command == '+':
        result = f"{number1}{command}{number2}={number1+number2}"
    elif command == '-':
        result = f"{number1}{command}{number2}={number1-number2}"
    print(result)