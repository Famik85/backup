# ### Задача 1: +
# **Умова:**
# Користувач вводить з клавіатури арифметичний вираз. Наприклад, 23+12. Необхідно
# вивести на екран результат виразу. У нашому прикладі це 35. Арифметичний вираз може
# складатися лише з трьох частин: число, операція, число. Можливі операції: +, -, *, /
# **Вхідні дані:**
# - Користувач вводить арифметичний вираз.
# **Вихідні дані:**
# - Вивести на екран результат обчислення виразу.

# Решение не супер,но другого я придумать не смог. Зато работает и обрабатывает числа любого размера.

# math_exp = input()
# l = []
# number_1 = []
# number_11 = ""
# number_2 = []
# number_22 = ""
# znak = ["+", "-", "*", "/"]
# for elem in math_exp:
#     l.append(elem)
# for elem in l:
#     if elem not in znak:
#         number_1 += elem
#     elif elem in znak:
#         znak = elem
#         break
# q = l.index(znak)
# number_2 = l[q+1:]
# for elem in number_2:
#     number_22 += elem
# number_22 = int(number_22)
# for elem in number_1:
#     number_11 += elem
# number_11 = int(number_11)
# if znak == "+":
#     print(number_11 + number_22)
# elif  znak == "-":
#     print(number_11 - number_22)
# elif  znak == "*":
#     print(number_11 * number_22)
# elif  znak == "/":
#     print(number_11 / number_22)

# ### Задача 2:  +
# **Умова:**
# У списку цілих чисел, заповненому випадковими числами, визначити мінімальний і
# максимальний елементи, порахувати кількість від'ємних елементів, порахувати кількість
# додатних елементів, порахувати кількість нулів. Результати вивести на екран.
# **Вхідні дані:**
# - Список цілих чисел, заповнений випадковими числами.
# **Вихідні дані:**
# - Мінімальний та максимальний елементи.
# - Кількість від'ємних, додатних та нульових елементів.

# l = [1, 2, -2, 3, -4, 0, 0, -78, 89]
# min_number = min(l)
# max_number = max(l)
# zero = 0
# zero_count = l.count(zero)
# positiv_count = 0
# negativ_count = 0
# for elem in l:
#     if elem > 0:
#         positiv_count += 1
#     elif elem < 0:
#         negativ_count += 1
# print(f"minimal element: {min_number}, maximum element: {max_number}")
# print(f"Negative element count: {negativ_count}, positiv element count: {positiv_count}, zero count: {zero_count}")


# ### Задача 3:
# **Умова:**
# Два списки цілих чисел заповнюються випадковими числами. Необхідно:
# 1. Сформувати третій список, що містить елементи обох списків.
# 2. Сформувати третій список, що містить елементи обох списків без повторень.
# 3. Сформувати третій список, що містить елементи, спільні для двох списків.
# 4. Сформувати третій список, що містить лише унікальні елементи кожного зі списків.
# 5. Сформувати третій список, що містить лише мінімальне та максимальне значення
# кожного зі списків.
# **Вхідні дані:**
# - Два списки цілих чисел, заповнені випадковими числами.
# **Вихідні дані:**
# 1. **Сформувати третій список, що містить елементи обох списків:**
# - Приклад вхідних даних: `[1, 2, 3], [4, 5, 6]`
# - Приклад вихідних даних: `[1, 2, 3, 4, 5, 6]`

# l1 = [1, 2, 3]
# l2 = [4, 5, 6]
# l3 = l1 + l2
# print(l3)

# 2. **Сформувати третій список, що містить елементи обох списків без повторень:**
# - Приклад вхідних даних: `[1, 2, 2, 3], [3, 4, 5]`
# - Приклад вихідних даних: `[1, 2, 3, 4, 5]`

# l1 = [1, 2, 2, 3]
# l2 = [3, 4, 5]
# l3 = []
# for elem in l1:
#     if elem not in l3:
#         l3.append(elem)
# for elem in l2:
#     if elem not in l3:
#         l3.append(elem)
# print(l3)

# 3. **Сформувати третій список, що містить елементи, спільні для двох списків:**
# - Приклад вхідних даних: `[1, 2, 3], [3, 4, 5]`
# - Приклад вихідних даних: `[3]`

# l1 = [1, 2, 3]
# l2 = [3, 4, 5]
# l3 = []
# for elem in l1:
#     if elem in l2:
#         l3.append(elem)
# print(l3)

# 4. **Сформувати третій список, що містить лише унікальні елементи кожного зі списків:**
# - Приклад вхідних даних: `[1, 2, 2, 3], [3, 4, 5, 5]`
# - Приклад вихідних даних: `[1, 2, 3, 4, 5]`

# l1 = [1, 2, 2, 3]
# l2 = [3, 4, 5, 5]
# l3 = []
# for elem in l1:
#     if elem not in l3:
#         if elem not in l2:
#             l3.append(elem)
# for elem in l2:
#     if elem not in l3:
#         if elem not in l1:
#             l3.append(elem)
# print(l3)

# 5. **Сформувати третій список, що містить лише мінімальне та максимальне значення
# кожного зі списків:**
# - Приклад вхідних даних: `[1, 2, 3, 4], [5, 6, 7, 8]`
# - Приклад вихідних даних: `[1, 4, 5, 8]`

# l1 = [1, 2, 3, 4]
# l2 = [5, 6, 7, 8]
# l3 = []
# l3.append(min(l1))
# l3.append(max(l1))
# l3.append(min(l2))
# l3.append(max(l2))
# print(l3)


# ### Задача 4:
# **На кортежі:**
# 1. **Створити кортеж:**
# - Створити кортеж, який містить кілька різних типів даних (цілі числа, рядки, дійсні
# числа). Вивести цей кортеж на екран.

# k = (1, 2, 3, "Hello", "World", 1.2, 0.1)
# print(k)

# 2. **Зміна кортежу:**
# - Створити кортеж чисел. Змінити один з елементів кортежу та вивести змінений кортеж
# на екран.

# Кортеж не изменяемый

# ### Задача 5:
# **На словники:**
# 1. **Операції зі словниками:**
# - Створити словник, що містить дані про деякий товар (наприклад, назва, ціна, кількість).
# Додати новий товар до словника та вивести оновлений словник на екран.

# d = {"product": {"name": "smartphone", "price": "1000", "quantity": "5"}}
# key = "new_product"
# value = {"name": "notebook", "price": "5000", "quantity": 1}
# d[key] = value
# print(d)

# 2. **Пошук та виведення:**
# - Створити словник, що містить інформацію про книги (назва, автор, рік видання).
# Здійснити пошук за назвою книги та вивести інформацію про неї.

# d = {"Rich Dad Poor Dad": {"author": "Robert Kiyosaki", "published": "1997"},
#      "The richest man in Babylon": {"auhtor": "George S. Clason", "published": "1926"},
#      "Miracle morning3": {"author": "John Murray", "published": "2017"}}
# search = input("Enter the book title: ")
# print(d[search])

# 3. **Видалення елементу:**
# - Створити словник, що містить дані про студентів (ім'я, прізвище, середній бал).
# Видалити інформацію про одного зі студентів та вивести оновлений словник на екран.

# d = {"student_1": {"name": "John", "surname": "Smith", "everage score": "3"},
#      "student_2": {"name": "Mark", "surname": "Peterson", "everage score": "3.7"},
#      "student_3": {"name": "Robert", "surname": "Wolf", "everage score": "4.2"},
#      "student_4": {"name": "Erik", "surname": "Klark", "everage score": "2.6"}}
# key = "student_2"
# deleted_student = d.pop(key)
# print(d)

# ### Задача 6:
# **На множини:**
# 1. **Операції з множинами чисел:**
# - Створити дві множини цілих чисел. Знайти їх об'єднання, різницю та перетин. Вивести
# результати на екран.

# s1 = {1, 2, 3, 4, 5, 6, 7, 8, 9}
# s2 = {2, 4, 5, 7, 8, 9, 11, 114, 15, 45}
# s3 = s1.union(s2)
# print(f"Combined set: {s3}")
# s4 = s2.difference(s1)
# s6 = s1.difference(s2)
# s7 = s4.union(s6)
# print(f"Set difference: {s7}")
# s5 = s1.intersection(s2)
# print(f"Set intersection: {s5}")

# 2. **Множина підмножин:**
# - Створити дві множини. Перевірити, чи є одна з них підмножиною іншої, та вивести
# результат.

# first_set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 114, 15, 45}
# second_set = {2, 4, 5, 6, 7, 8, 9}
# if first_set <= second_set:
#     print(f"The set {first_set} is included in the set {second_set}")
# elif second_set <= first_set:
#     print(f"The set {second_set} is included in the set {first_set}")

# 3. **Операції з символами:**
# - Створити дві множини символів (літери алфавіту). Знайти їх об'єднання, різницю та
# перетин. Вивести результати на екран.

# s1 = {"a","b","c","d","s","f"}
# s2 = {"a","d","y","d","r"}
# s3 = s1.union(s2)
# print(f"Combined set: {s3}")
# s4 = s2.difference(s1)
# s6 = s1.difference(s2)
# s7 = s4.union(s6)
# print(f"Set difference: {s7}")
# s5 = s1.intersection(s2)
# print(f"Set intersection: {s5}")

# 4. **Додавання та видалення елементів:**
# - Створити множину слів. Додати нове слово та видалити існуюче. Вивести оновлену
# множину на екран

# s = {"Hello", "God", "Peace", "Kingdom", "Wolrd"}
# s.add("New")
# s.remove("Peace")
# print(s)
