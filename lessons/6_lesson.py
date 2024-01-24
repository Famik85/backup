while True:
    result = 0
    try:
        n1 = int(input("Enter your number1 : "))
        command = str(input("Enter your command :"))
        n2 = int(input("Enter your number2: "))
        result = 0
        if command == "*":
            result = f"{n1}{command}{n2}={n1 * n2}"
        elif command == "/":
            result = f"{n1}{command}{n2}={n1 / n2}"
    except ValueError:
        print("Вы ввели некорректное значение, попробуйте еще раз")
    except ZeroDivisionError:
        print("Вы пытаетесь поделить на 0")
    else:
        print("Good work!")
    finally:
        print(result)
