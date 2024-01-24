# set   множина     змінний, ітерований, не індексований тип данних

s = {1, 2, 3, 4, 5, 6, 3, 4, 5, 1, 2}

print(3 in s)

print(s)

l = 1, 2, 3, 4, 5, 6, 3, 4, 5, 1, 2
print(l)
l1 = set(l)

print(l1)

# frozenset  незмінна множина     незмінний, ітерований, не індексований тип данних

l2 = frozenset(l)
print(l2)

# dict dictionary словник змінний, ітерований, не індексований тип данних
# послідовніть типу ключ: значення
# ключем може бути БУДЬ-ЯКИЙ НЕЗМІННИЙ тип данних. значення - будь-який тип данних

d = {'a': 1, 'b': 2, 'c': 3, 'd': [1, 2, 3], 'e': {'a': 1, 'b': 2, 'c': 3, 'd': [1, 2, 3]}}
print(d)
import pprint as p

p.pprint(d)

print(d['b'])
d['b'] = 22
print(d['b'])
d['f'] = True
print(d['f'])
print(d)

for k in d:
    print(k, d[k])

print(d.items())
for key, value in d.items():
    print(key, value)

colors = {(255, 0, 0): 'red', (0, 255, 0): 'green', (0, 0, 255): 'blue', (103, 78, 167): 'purple',
          (212, 224, 54): 'mustard', 'red': (255, 0, 0), 'green': (0, 255, 0)}
# https://www.color-hex.com/

while True:
    command = str(input("Enter command: [c], [r], [u], [d] : "))
    # CRUD
    # Create
    if command.lower() == 'c':
        key = str(input("Enter color name : "))
        value = str(input("Enter color value : "))
        colors[key] = value
    # Read
    elif command.lower() == 'r':
        for key, value in colors.items():
            print(key, value)
    # Update
    elif command.lower() == 'u':
        key = str(input("Enter color name : "))
        new_value = str(input("Enter color value : "))
        if key not in colors:
            way = str(input("This key aren't present in colors. Are you want add it?: [y] or [n] : "))
            if way == 'y':
                colors[key] = new_value
        elif key in colors:
            colors[key] = new_value

    # Delete
    elif command.lower() == 'd':
        key = str(input("Enter color name : "))
        result = colors.pop(key, "Not present")
        print(f"Color {key} deleted with result {result}")
