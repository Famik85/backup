# Files

# Create
# f = open("test1.txt", "wt")
# f.write("Hello World!\n")
# f.write("My name is Alex")
#
# f.close()
#
# # # Read
# # f = open("test1.txt", "rt")
# # a = f.read()
# # print(a)
#
# # f.close()
#
# #Append
#
#
# f = open("test1.txt", "at")
# f.write("\nRun Test\n")
# f.write("First test")
#
#
# f.close()
#
# # Read
# f = open("test1.txt", "rt")
# a = f.read()
# print(a)

# create random numbers 100-999
import random

f = open("test2.txt", "wt")
for i in range(200):
    a = str(random.randint(100,150))
    f.write(a)
    f.write("\n")
f.close()

# Вывести простые числа
# calc = open("test2.txt", "rt")
# l = calc.readlines()
# for line in l:
#     flag = True
#     for i in range(2, int(line[:-1])):
#         if int(line[:-1]) % i == 0:
#             flag = False
#     if flag:
#         print(line[:-1])
# calc.close()

# Вывести числа в порядке возростания
# calc = open("test2.txt", "rt")
# l = calc.readlines()
# l.sort()
# for line in l:
#     print(line[:-1])
# calc.close()

# Вывести уникальные числа в порядке возростания
# calc = open("test2.txt", "rt")
# l = calc.readlines()
# l = set(l)
# l = list(l)
# l.sort()
# for line in l:
#     print(line[:-1])
# calc.close()