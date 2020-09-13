def my_func1(x, y):
    return round(x ** y, 3)


def my_func2(x, y):
    result = 1
    for el in range(abs(y)):
        result *= x
    return 1/result


def check_x(x):
    while True:
        if x > '0':
            try:
                float(x)
                return float(x)
            except ValueError:
                x = input("Try again, enter real positive number x: ")
        else:
            x = input("Try again, enter real positive number x: ")


def check_y(y):
    while True:
        if y < '0':
            try:
                int(y)
                return int(y)
            except ValueError:
                y = input("Try again, enter integer negative number y: ")
        else:
            y = input("Try again, enter integer negative number y: ")


print("Hello, you need raise 'x' to negative power '-y': x ** (-y)")
x = (input("Enter real positive number x: "))
x = check_x(x)
y = input("Enter integer negative number y: ")
y = check_y(y)

print(f"First function: {x} ** ({y}) = {my_func1(x, y)}")
print(f"Second function: {x} ** ({y}) = {my_func2(x, y)}")

