# # Файли
#
# # #Create
# # f = open("test1.txt", "wt")
# # f.write("Hello World!\n")
# # f.write("My name is Andrii\n")
# # f.close()
#
# #Read
# f = open("test1.txt", "rt")
# a = f.read()
# print(a)
# f.close()
#
# #Append
# f = open("test1.txt", "at")
# f.write("Run test\n")
# f.write("First test\n")
# f.close()
#
# #X
# try:
#     f = open("test1.txt", "xt")
#     f.write("Run test\n")
#     f.write("First test\n")
#     f.close()
# except:
#     print("We have this file")
#
#
import random

# Створення файлу
f = open("test2.txt", "wt")
for i in range(200):
    a = str(random.randint(100, 150))
    f.write(a)
    f.write("\n")
f.close()

# Вивести прості числа
calc = open("test2.txt", "rt")
l = calc.readlines()
for line in l:
    flag = True
    for i in range(2, int(line[:-1])):
        if int(line[:-1]) % i == 0:
            flag = False
    if flag:
        print(line[:-1])
calc.close()

# Висвести числа в порядку зростання
calc = open("test2.txt", "rt")
l = calc.readlines()
l.sort()
for line in l:
    print(line[:-1])
calc.close()

print()
# Висвести унікальні числа в порядку зростання
calc = open("test2.txt", "rt")
l = calc.readlines()
l = set(l)
l = list(l)
l.sort()
for line in l:
    print(line[:-1])
calc.close()

book = open("example.html", "rt")
a = book.readlines()
for line in a:
    if 'HREF="http' in line:
        b = line[line.find("http"):line.find('" ADD_DATE')]
        print(b)
book.close()