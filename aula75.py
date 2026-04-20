import sys
try:
    def duplicate(*args):
        total = 1
        for number in args:
            total *= number
        return total
    x = input("Type a whole number: ")

    x_int = int(x)
except ValueError:
    print("Please type a whole number.")
    sys.exit()
multiplicate = duplicate(x_int, x_int)
print(multiplicate)

def triplicate(*args):
    total = 1
    for number in args:
        total *= number
    return total
multiplicate = triplicate(x_int, x_int, x_int)
print(multiplicate)

def quadruplicate(*args):
    total = 1
    for number in args:
        total *= number
    return total
multiplicate = quadruplicate(x_int, x_int, x_int, x_int)
print(multiplicate)