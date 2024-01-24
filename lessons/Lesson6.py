# #Exception
#
# # a = 4
# # b = 2
# # print(a/b)
#
#
# # a = 4
# # b = 0
# # try:
# #     print(a/b)
# # except: # Голе виключення
# #     print("Ops...")
# #
# # print("Enter something else")
#
#
# # a = 4
# # b = 2
# # try:
# #     print(a/b)
# # except ZeroDivisionError:
# #     print("You cannot div to zero")
# #
# # except TypeError:
# #     print("Incorrect type")
# #
# # except NameError:
# #     print("Add all variable")
# #
# # except: # Голе виключення
# #     print("Ops...")
# #
# # print("Enter something else")
#
# a = 4
# b = 2
# try:
#     print(a/b)
#
# except ZeroDivisionError:           # if
#     print("You cannot div to zero")
#
# except TypeError:                   #elif
#     print("Incorrect type")
#
# except NameError:                   #elif
#     print("Add all variable")
#
# except: # Голе виключення           #else
#     print("Ops...")
#
# else:                               # Буде використане, якщо не було помилок
#     print("Program finish corretly")
#
# finally:                            # Буде виконане в будь якому разі
#     print("Exit")
#
#

while True:
    result = 0
    try:
        n1 = int(input("Enter your number1 : "))
        command = str(input("Enter your command : "))
        n2 = int(input("Enter your number2 : "))

        if command == '*':
            result = f"{n1}{command}{n2}={n1*n2}"
        elif command == '/':
            result = f"{n1}{command}{n2}={n1/n2}"
    except ValueError:
        print("Ви ввели некорректне значення, спробуйте ще")
    except ZeroDivisionError:
        print("Ви намагаєтесь поділити на 0")
    else:
        print("Good work!")
    finally:
        print(result)



