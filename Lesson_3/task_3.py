def sum_max(a, b, c):
    try:
        temp = [float(a), float(b), float(c)]
    except ValueError as err:
        print("You need enter number, please try again")
        return
    return sum(temp) - min(temp)


print(sum_max(input("Enter number 1: "), input("Enter number 2: "), input("Enter number 3: ")))
