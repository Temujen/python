def div_function(var1, var2):
    try:
        result = float(var1) / float(var2)
        return round(result, 2)
    except (ZeroDivisionError, ValueError) as err:
        print(f"{err}\n Please try again")


number1 = input("Enter first number: ")
number2 = input("Enter second number: ")
print(div_function(number1, number2))
