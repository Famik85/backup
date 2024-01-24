# s = "Hello, World"
# print(s)
#
# print(s[0], s[1], s[2], s[3])

# Str -  неизменяемый, индексированный, итерированный тип данных

# неизменяемый
# s = "Hello"
# s = s + " Wolrd!"

# индексированный
# print(s[0], s[1], s[2], s[3])

# итерированный
# s = "Hello World"

# n = "Alexandr Reva"
#
# print(n[7], n[2], n[11], n[2], n[0], n[1],) #Раскрывать
# print(n[7], n[4], n[11], n[2], n[5])     # Ворон
# print(n[2], n[1], n[2], n[11], n[2], n[5])   # Одиннадцать

# s = "Hello World"
# print(s[0:5])#Hello
# print(s[6:11])#World
#
# print(s[:5])#Hello
# print(s[6:])#World!
# print(s[::-1])#!dlroW olleH
#
# new_word = s[6:9] + s[10]
# print(new_word)
#
# s = "John's"
# s = 'Jon"s'
# print("John's John\"s")
#
# print("Hello " * 5)
# print(len(s))
#
# s = "Hello World!"
# count = 0
# letter = "l"
# for elem in s:
#     if elem == letter:
#         count = count + 1
# print(count)
# print(s.count(letter))


# q = input("Enter your stroke: ")
# print(len([i for i in q if i.isdigit()]))
# print(len([i for i in q if i.isalpha()]))

# password = 'gnfgvmnfg435D'
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
#     print("Bad password")

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
        result = f"{number1}{command}{number2}={number1 + number2}"
    elif command == '-':
        result = f"{number1}{command}{number2}={number1 - number2}"
    print(result)