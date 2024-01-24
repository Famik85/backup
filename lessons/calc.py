# import calc_func


# n1 = 5
# n2 = 3
#
# print(calc_func.plus(n1,n2))

import calc_func as c

# n1 = 5
# n2 = 3
#
# print(c.plus(n1, n2))

while True:
    number1 = int(input("Enter number1 : "))
    command = str(input("Enter command : "))
    number2 = int(input("Enter number2 : "))
    result = ''
    if command == "+":
        result = f"{number1}{command}{number2}={c.plus(number1, number2)}"
    elif command == "-":
        result = f"{number1}{command}{number2}={c.minus(number1, number2)}"
    elif command == "*":
        result = f"{number1}{command}{number2}={c.mult(number1, number2)}"
    elif command == "/":
        result = f"{number1}{command}{number2}={c.divis(number1, number2)}"
    print(result)