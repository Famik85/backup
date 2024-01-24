# Завдання 1:
#
# Дано два текстових файли. Визначте, чи збігаються їхні рядки.
# Якщо ні, виведіть відмінний рядок з кожного файлу.

# f1 = open("test1.txt", "rt")
# f2 = open("test2.txt", "rt")
# lines1 = f1.readlines()
# lines2 = f2.readlines()
# min_length = min(len(lines1), len(lines2))
# for i in range(min_length):
#     if lines1[i] != lines2[i]:
#         print(f"Difference in line {i + 1}:\nFile 1: {lines1[i]}File 2: {lines2[i]}")
#
# if len(lines1) > len(lines2):
#      for i in range(min_length, len(lines1)):
#        print(f"Additional line in File 1, line {i + 1}: {lines1[i]}")
#
# elif len(lines2) > len(lines1):
#     for i in range(min_length, len(lines2)):
#         print(f"Additional line in File 2, line {i + 1}: {lines2[i]}")

# Завдання 2:
#
# Даний текстовий файл. Створіть новий файл та запишіть у нього наступну статистику
# щодо вихідного файлу:
#
# = Кількість символів;
#
# = Кількість рядків;
#
# = Кількість голосних букв;
#
# = Кількість приголосних букв;
#
# = Кількість цифр.

# f1 = open("test1.txt", "rt")
# f2 = open("test2.txt", "wt")
# content = f1.read()
# char_count = len(content)
# f2.write(f"Char count: {char_count}\n")
# line_count = content.count("\n") + 1
# f2.write(f"Line count: {line_count}\n")
# vowels_count = 0
# consonants_count = 0
# digits_count = 0
# for char in content:
#     if char.lower() in "eyuioaуеоаыяиюэ":
#         vowels_count += 1
# f2.write(f"Vowels count: {vowels_count}\n")
# for char in content:
#     if char.isalpha() and char.lower() not in "eyuioaуеоаыяиюэ":
#         consonants_count += 1
# f2.write(f"Consonants count: {consonants_count}\n")
# for char in content:
#     if char.isdigit():
#         digits_count += 1
# f2.write(f"Digits count: {digits_count}\n")

# Завдання 3:
#
# Даний текстовий файл. Видаліть з нього останній рядок.
# Результат запишіть у інший файл.

# f1 = open("test1.txt", "rt")
# f2 = open("test2.txt", "wt")
# lines = f1.readlines()
# if lines:
#     lines.pop()
# f2.writelines(lines)

# Завдання 4:
#
# Даний текстовий файл.
# Знайдіть довжину найдовшого рядка.

# f = open("test1.txt", "rt")
# lines = f.readlines()
# if not lines:
#     print("Your file does not contain lines")
# else:
#     longest_line_length = max(len(line) for line in lines)
#     print(f"Longest line length: {longest_line_length}")