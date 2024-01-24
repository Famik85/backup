# Завдання 1
# Користувач вводить три цифри з клавіатури. Залежно від вибору користувача, програма виводить на екран суму трьох чисел
# або добуток трьох чисел.
# a = int(input("Enter number one: "))
# b = int(input("Enter number two: "))
# c = int(input("Enter number three: "))
# d = int(input("If you want to multiply numbers enter 1, If you want to add numbers enter 2: "))
# if d == 1:
#     print(a * b * c)
# elif d == 2:
#     print(a + b + c)
# else:
#     print("Enter a valid character ")




# Завдання 2
# Користувач вводить три цифри з клавіатури. Залежно від вибору користувача програма виводить на екран максимум із трьох,
# мінімум із трьох або середнеарифметичне трьох чисел.

# a = int(input("Enter number one: "))
# b = int(input("Enter number two: "))
# c = int(input("Enter number three: "))
# d = int(input("Max - enter 1, Min - enter 2, Average - enter 3: "))
# if d == 1:
#     if a > b:
#         if a > c:
#             print(a)
#         else:
#             print(c)
#     elif b > a:
#         if b > c:
#             print(b)
#         else:
#             print(c)
# elif d == 2:
#     if a < b:
#         if a < c:
#             print(a)
#         else:
#             print(c)
#     elif b < a:
#         if b < c:
#             print(b)
#         else:
#             print(c)
# elif d == 3:
#     print((a + b + c) / 3)
# else:
#     print("Enter a valid character ")

# Завдання 3
# Користувач вводить з клавіатури номер дня тижня
# (1-7). Необхідно вивести на екран назви дня тижня. Наприклад, якщо 1, то на екрані напис понеділок, 2 - вівторок і т.д.

# a = int(input("Enter the day of the week: "))
# if a == 1:
#     print("Monday")
# elif a == 2:
#     print("Tuesday")
# elif a == 3:
#     print("Wednesday")
# elif a == 4:
#     print("Thursday")
# elif a == 5:
#     print("Friday")
# elif a == 6:
#     print("Saturday")
# elif a == 7:
#     print("Sunday")
# else:
#     print("Enter a valid character ")


# Завдання 4
# Користувач вводить з клавіатури номер місяця (1-12). Необхідно вивести на екран назву місяця.
# Наприклад, якщо 1, то на екрані напис січень, 2 - лютий і т.д.

# a = int(input("Enter month: "))
# if a == 1:
#     print("January")
# elif a == 2:
#     print("February")
# elif a == 3:
#     print("March")
# elif a == 4:
#     print("April")
# elif a == 5:
#     print("May")
# elif a == 6:
#     print("June")
# elif a == 7:
#     print("July")
# elif a == 8:
#     print("August")
# elif a == 9:
#     print("September")
# elif a == 10:
#     print("October")
# elif a == 11:
#     print("November")
# elif a == 12:
#     print("December")
# else:
#     print("Enter a valid character ")

# Завдання 5
# Користувач вводить із клавіатури число. Якщо число
# більше нуля потрібно вивести напис "Number is positive", якщо менше нуля "Number is negative", якщо дорівнює
# нулю «Number is equal to zero»

# a = int(input("Enter the number: "))
# if a > 0:
#     print("Number is positive")
# elif a == 0:
#     print("Number is equal to zero")
# else:
#     print("Number is negative")



# Завдання 6
# Користувач вводить два числа. Визначити, чи рівні ці числа, і, якщо ні, вивести їх на екран у порядку зростання.

# a = int(input("Enter number one: "))
# b = int(input("Enter number two: "))
# if a == b:
#     print("Numbers are equal")
# elif a != b:
#     if a > b:
#         print(b, a)
#     else:
#         print(a, b)

# Завдання 7
# Користувач вводить з клавіатури два числа (початок та кінець діапазону). Потрібно проаналізувати всі числа в цьому
# діапазоні за таким правилом: якщо число кратно 7 його треба виводити на екран.

# a = int(input("Enter number one: "))
# b = int(input("Enter number two: "))
# while a < b:
#     if a % 7 == 0:
#         print(a)
#     a = a + 1


# Завдання 8  +
# Користувач вводить з клавіатури два числа (початок та кінець діапазону). Потрібно проаналізувати все числа у цьому діапазоні.
# Потрібно вивести на екран:
# 1. Усі числа діапазону;
# 2. Усі числа діапазону у спадному порядку;
# 3. Усі числа, кратні 7;
# 4. Кількість чисел, кратних 5.

# a = int(input("Enter number one: "))
# b = int(input("Enter number two: "))
# c = 0
# for i in range(a, b + 1):     #1
#     print(i)
#
# for i in range(b, a - 1 , -1):              #2
#     print(i)
#
#
#
# for i in range(a, b + 1):          #3
#     if i % 7 == 0:
#         print(i)
#
#
# for i in range(a, b + 1):           #4
#     if i % 5 == 0:
#         c = c + 1
# print(c)


# Завдання 9
# Користувач вводить з клавіатури два числа (початок та кінець діапазону). Потрібно проаналізувати усі числа у
# цьому діапазоні. Виведення на екран має відбуватися за правилами, наведеними нижче. Якщо число
# кратне 3 (ділиться на 3 без залишку), потрібно вивести слово Fizz. Якщо число разів 5 потрібно
# вивести слово Buzz. Якщо число кратно 3 та 5 потрібно вивести Fizz Buzz. Якщо число не раз не 3 і 5 потрібно вивести саме число.

# a = int(input("Enter number one: "))
# b = int(input("Enter number two: "))
# for i in range(a, b + 1):
#     if i % 5 == 0:
#         if i % 3 == 0:
#             print("Fizz Buzz")
#         else:
#             print("Buzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     else:
#         print(i)
