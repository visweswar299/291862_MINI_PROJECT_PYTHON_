from datetime import datetime


def add(a, b):
    return a+b


def subtract(a, b):
    return a-b


def multiply(a, b):
    return a*b


def divide(a, b):
    return a/b


def modulo(a, b):
    return a % b


def power(a, b):
    return a ** b


while True:
    f = open("myfile.txt", "a")
    print("\n-------------------------------------------------------------------------------------------\n")
    print(datetime.now())
    print(datetime.now(), file=f)
    input1 = input("Enter a number or type 'STOP' to turn off: ")
    if input1 == "STOP" or input1 == "stop" or input1 == "Stop":
        print("Turning off.")
        print("Turning off.", file=f)
        break
    elif not input1.isdigit():
        print("This is not a valid number.")
        continue
    else:
        number1 = int(input1.strip())
        print("Enter a number or type 'STOP' to turn off:" + str(number1), file=f)
    operator = input("Enter an operation (+, -, *, /, %, or **): ")
    operator = operator.strip()
    print("Enter an operation (+, -, *, /, or %):" + str(operator), file=f)
    input2 = input("Enter another number: ")
    if not input2.isdigit():
        print("This is not a valid number.")
        continue
    else:
        number2 = int(input2.strip())
        print("Enter a number or type 'STOP' to turn off:" + str(number2), file=f)
    if operator == '+':
        ans = add(number1, number2)
    elif operator == '-':
        ans = subtract(number1, number2)
    elif operator == '*':
        ans = multiply(number1, number2)
    elif operator == '/':
        ans = divide(number1, number2)
    elif operator == '%':
        ans = modulo(number1, number2)
    elif operator == '**':
        ans = power(number1, number2)
    else:
        print("You did not enter a valid operation.")
        print("You did not enter a valid operation.", file=f)
        continue
    print(number1, operator, number2, "=", ans)
    print(str(number1), str(operator), str(number2), "=", str(ans), file=f)
    f.close()
