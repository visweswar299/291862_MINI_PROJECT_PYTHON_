import datetime


def get_time():
    return datetime.datetime.now()


def take(k):
    if k == 1:
        c = int(input("enter 1 for exercise and 2 for food:"))
        if c == 1:
            value = input("type here\n")
            with open("viswa-ex.txt", "a") as op:
                op.write(str([str(get_time())]) + ": " + value + "\n")
            print("successfully written")
        elif c == 2:
            value = input("type here\n")
            with open("viswa-food.txt", "a") as op:
                op.write(str([str(get_time())]) + ": " + value + "\n")
            print("successfully written")
    else:
        print("plz enter valid input!")


def retrieve(k):
    if k == 1:
        c = int(input("enter 1 for exercise and 2 for food:"))
        if c == 1:
            with open("viswa-ex.txt") as op:
                for i in op:
                    print(i, end="")
        elif c == 2:
            with open("viswa-food.txt") as op:
                for i in op:
                    print(i, end="")
    else:
        print("plz enter valid input!")


print("health management system: ")
a = int(input("Press 1 for log the value and 2 for retrieve: "))


if a == 1:
    b = int(input("Press 1 for viswa: "))
    take(b)
else:
    b = int(input("Press 1 for viswa: "))
    retrieve(b)
