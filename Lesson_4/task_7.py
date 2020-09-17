def fact(a):
    result = 1
    for i in range(1, a + 1):
        result *= i
        yield result


try:
    generator = fact(int(input("Enter integer number: ")))
    for el in generator:
        print(el)
except ValueError:
    print("Enter only integer number, please try again")
