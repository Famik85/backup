# # IDE
# # Integrated Development Enviroment
#
# # Variables
# age = 13
# gender = "male"  # "female"
#
# # Conditions
# if age < 18:
#     print("You are a child")
# else:
#     print("You are an adult")
#
# #   >    <    >=     <=     ==     !=
# print(5 > 3)  # True
# print(5 < 3)  # False
# print(5 >= 3)  # True
# print(5 <= 5)  # True
# print(4 == 5)  # False
# print(4 != 3)  # True
#
# # Ctrl + Alt + L    -   format to PEP8
#
# # < 120 - проход запрещен
# # < 140 -
# height = 130
# if height < 120:
#     print("Проход запрещен")
# elif height < 140:
#     print("Ограничено")
# else:
#     print("Проход разрешен")
#
# age = 13
# if age < 13:
#     print("You are a child")
# elif age < 18:
#     print("You are a teen")
# else:
#     print("You are an adult")

# Loop

# while     цикл с условием
# for       цикл с параметром
# a = 0
# while a < 10:  # while для работы должен получать True
#     print(a)
#     a = a + 1  # инкремент

# a = 1
# b = 36
# while a < b:
#     if a % 2 != 0:
#         print(a)  # Odd (нечетные)
#     a = a + 1

# for i in 1,2,3,4,5,6,7,8,9,:
#     print(i)

# a = 1
# b = 36
# for i in range(a, b + 1):
#     if i % 2 != 0:
#         print(i)
#
# a = 1
# b = 36
# c = a
# while a < b:
#     a = a + 1
#     c = c + a
# print(c)
#
#
# a = 1
# b = 36
# summa = 0
# for i in range(a,b + 1):
#     summa = summa + i
# print(summa)
#
# #break - остановить цикл
# a = 1
# b = 30
# while a <= b:
#     if a % 5 == 0:
#         print(a)
#         break
#     a = a + 1
#
# #continue пропускает итерацию цикла
# a = 1
# b = 30
# while a <= b:
#     a = a + 1
#     if a % 5 == 0:
#         continue
#     print(a)

