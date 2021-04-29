from datetime import datetime

today = datetime.today()

print("Current date =", today)


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
    return a**b


def square(a):
    return a*a


def factorial(a):
    if a == 1 or a == 0:
        return 1
    else:
        fact = 1
        for i in range(1, a+1):
            fact *= i
        return fact


