# import datetime to use date and time
from datetime import datetime


# add function to find addition of two numbers
def add(a, b):
    return a+b


# subtract function to find subtraction of two numbers
def subtract(a, b):
    return a-b


# multiplication function to find (n times of m number)
def multiply(a, b):
    return a*b


# division function to find quotient of the numbers
def divide(a, b):
    return a/b


# modulus function to find remainder of the numbers
def modulo(a, b):
    return a % b


# power function to find power of numbers
def power(a, b):
    return a ** b


while True:
    # myfile.txt is to store the calculated values.
    f = open("myfile.txt", "a")
    print("\n-------------------------------------------------------------------------------------------\n")
    print(datetime.now())
    print(datetime.now(), file=f)
    '''
    enter first number to calculate other wise type stop to turn off
    if entered value is not digit then it shows invalid number
    '''
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
    # operator - enter what operation do you want
    operator = input("Enter an operation (+, -, *, /, %, or **): ")
    operator = operator.strip()
    # if you entered other than providing options it will show entered operation is invalid
    print("Enter an operation (+, -, *, /, or %):" + str(operator), file=f)
    # enter second number to calculate
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
    # file closing
    f.close()
