from datetime import datetime


def add(operand1, operand2):
    """
    :param operand1: first input to add
    :param operand2: second input to add
    :return: addition of first number and second number to get total sum
    """
    return operand1 + operand2


def subtract(operand1, operand2):
    """
        :param operand1: first input to subtract
        :param operand2: second input to subtract
        :return: subtraction of first number and second number to get remaining total(value)
    """
    return operand1 - operand2


def multiply(operand1, operand2):
    """
        :param operand1: first input to multiply
        :param operand2: second input to multiply
        :return: multiplication of first number and second number to get total value
    """
    return operand1 * operand2


def divide(operand1, operand2):
    """
        :param operand1: first input as dividend
        :param operand2: second input as divisor
        :return: division of first number and second number to get quotient
    """
    if operand1 == 0:
        return 0
    elif operand2 == 0:
        return None
    else:
        return operand1 / operand2


def modulo(operand1, operand2):
    """
        :param operand1: first input as dividend
        :param operand2: second input as divisor
        :return: addition of first number and second number to get remainder
    """
    if operand1 == 0:
        return 0
    elif operand2 == 0:
        return None
    else:
        return operand1 % operand2


def power(operand1, operand2):
    """
        :param operand1: first input as base
        :param operand2: second input as power
        :return: power of first number with second number
    """
    return operand1 ** operand2


while True:
    # myfile is to store the calculated values.
    with open("myfile.txt", "a") as f:

        print("\n-------------------------------------------------------------------------------\n")
        print(datetime.now())
        print(datetime.now(), file=f)
        # enter first number to calculate other wise type stop to turn off
        # if entered value is not digit then it shows invalid number
        input1 = input("Enter a number or type 'STOP' to turn off: ")
        if input1 == 'STOP' or input1 == 'stop' or input1 == 'Stop':
            print("Turning off.")
            print("Turning off.", file=f)
            break
        elif not input1.isdigit():
            print("This is not a valid number.")
            print("This is not a valid number.", file=f)
            continue
        else:
            number1 = int(input1.strip())
            print("Enter a number or type 'STOP' to turn off:" + str(number1), file=f)
        # operator - enter what operation do you want from the given symbol
        # otherwise it will show invalid operator.
        operator = input("Enter an operation (+, -, *, /, %, or **): ")
        operator = operator.strip()
        print("Enter an operation (+, -, *, /, or %):" + str(operator), file=f)
        # enter second number to calculate
        input2 = input("Enter another number: ")
        if not input2.isdigit():
            print("This is not a valid number.")
            print("This is not a valid number.", file=f)
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
