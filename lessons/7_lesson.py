# import random
#
# f = open("test1.txt", "wt")
# for i in range(200):
#     f.write(str(random.randint(100, 999)))
#     f.write('\n')
# f.close()

# test = open("test1.txt", "rt")
# odd = open("odd.txt", "wt")
# even = open("even.txt", "wt")
# word = test.readline()
#
# while word:
#     letters = word[:-1]
#     number = int(letters)
#     if number % 2 == 0:
#         even.write(word)
#     elif number % 2 != 0:
#         odd.write(word)
#
#     word = test.readline()
#
# odd.close()
# even.close()
# test.close()

# test = open("test1.txt", "rt")
# odd = open("odd.txt", "wt")
# even = open("even.txt", "wt")
# word = test.readline()
#
# while word:
#     try:
#          letters = word[:-1]
#          number = int(letters)
#          if number % 2 == 0:
#               even.write(word)
#          elif number % 2 != 0:
#               odd.write(word)
#     except:
#         continue
#     finally:
#         word = test.readline()
#
# odd.close()
# even.close()
# test.close()

# import json
#
# # Serialisation
# notes = {"a": 1, "b": 2, "c": 3, "d": {"e": 4, "f": 5, "g": 6} }
# print(json.dumps(notes, sort_keys=True, indent=4))
# with open("something.json", "wt") as file:
#     json.dump(notes, file)
#
# # Deserialisation
#
# a = json.dumps(notes, sort_keys=True, indent=4)
# d_a = json.loads((a))
# print(d_a)
#
# with open("something.json", "rt") as file:
#     d_q = json.load(file)
# print(d_q)

# Оголошення функціі
# def some_file():
#     import random
#     f = open("test2.txt", "wt")
#     for i in range(200):
#         f.write(str(random.randint(100, 999)))
#         f.write('\n')
#     f.close()
#
# # Виклик функціі
# some_file()

# def some_file(name="test0", lenght=200):
#     import random
#     f = open(f"{name}.txt", "wt")
#     for i in range(lenght):
#         f.write(str(random.randint(100, 999)))
#         f.write('\n')
#     f.close()
#
#
#
# some_file()
# some_file("test10",400)

# def some_file(name):
#     f = open(f"{name}.txt", "rt")
#     print(f.readlines())
#     f.close()
#
# some_file("test1")

#  Порядок атрибутов функции

def something(a, b, c=3, d=5, *e, **f): # a, b - упорядоченные атрибуты (positional arguments)
# c, d - атрибуты по умолчанию (можно не указывать)
# *e - args неупорядоченные аргументы
# **f - kwargs key word arguments