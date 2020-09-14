def my_func1(x, y):
    return round(x ** y, 5)


def my_func2(x, y):
    result = 1
    for el in range(abs(y)):
        result *= x
    return round(1/result, 5)


def check_x(arg):
    while True:
        if arg > '0':
            try:
                float(arg)
                return float(arg)
            except ValueError:
                arg = input("Try again, enter real positive number x: ")
        else:
            arg = input("Try again, enter real positive number x: ")


def check_y(arg):
    while True:
        if arg < '0':
            try:
                int(arg)
                return int(arg)
            except ValueError:
                arg = input("Try again, enter integer negative number y: ")
        else:
            arg = input("Try again, enter integer negative number y: ")


print("Hello, you need raise 'x' to negative power '-y': x ** (-y)")
x = (input("Enter real positive number x: "))
x = check_x(x)
y = input("Enter integer negative number y: ")
y = check_y(y)

print(f"First function: {x} ** ({y}) = {my_func1(x, y)}")
print(f"Second function: {x} ** ({y}) = {my_func2(x, y)}")

