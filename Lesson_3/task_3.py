def sum_max(a, b, c):
    try:
        temp = [float(a), float(b), float(c)]
    except ValueError as err:
        print("You need enter number, please try again")
        return
    temp.pop(temp.index(min(temp)))
    return sum(temp)


print(sum_max(input("Enter number 1: "), input("Enter number 2: "), input("Enter number 3: ")))
