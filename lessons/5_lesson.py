# list    список       Изменяемый, Индексируемый, Итерируюмый

# Изменяемый

l = [1, 2, 3, 4, 5, "Hello", True, "Hello", 3.6, [1, 2, 3]]
print(l[2])
print(l)
l[2] = 10
print(l)

# Индексируемый
print(l[5])
print()

# Итерируюмый
for elem in l:
    print(elem)

# Кол-во определенных элементов в цикле

# word = "Hello"
# count = 0
# for elem in l:
#     if word == elem:
#         count = count + 1
#
# print(f"Count of word {word} : {count}")

l = [1, 2, 3, 4, 5, "Hello World!", True, "Hello World!!!111", 3.6, [1, 2, 3]]
word = "3"
count = 0
for elem in l:
    if word in elem:
        count += 1
print(f"Count of word {word} : {count}")

# tuple    кортеж       не изменяемый, Индексируемый, Итерируюмый
t = (1, 2, 3, 4, 5, "Hello World!", True, "Hello World!!!111", 3.6, [1, 2, 3])

colors = {(255, 0, 0): "red", (0, 255, 0): "green", (0, 0, 255): "blue", (103, 78, 167): "purple",
          (212, 224, 554): "mustard", "red": (255, 0, 0), "green": (0, 255, 0)}
while True:
    command = str(input("Enter command: [c], [r], [u], [d] : "))
    # CRUD
    # Create
    if command.lower() == "c":
        key = str(input("Enter color name : "))
        value = str(input("Enter color value : "))
        colors[key] = value
    # Read
    elif command.lower() == "r":
        for key, value in colors.items():
            print(key, value)
    # Update
    elif command.lower() == "u":
        key = str(input("Enter color name : "))
        new_value = str(input("Enter color value : "))
        if key not in colors:
            way = str(input("This key aren't present in colors. Are you want add it?: [y] or [n] : "))
            if way == "y":
                colors[key] = new_value
        elif key in colors:
            colors[key] = new_value
    # Delete
    elif command.lower() == "d":
        key = str(input("Enter color name : "))
        result = colors.pop(key, "Not present")
        print(f"Color {key} deleted with result {result}")