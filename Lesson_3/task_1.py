def div_function(var1, var2):
    try:
        result = var1 / var2
        return round(result, 2)
    except ZeroDivisionError as err:
        print(f"{err}, Please try again")


number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))
print(div_function(number1, number2))
