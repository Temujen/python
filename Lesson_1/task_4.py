number = int(input("Enter number: "))
maximum = number % 10
while number:
    if maximum < number % 10:
        maximum = number % 10
    number = number // 10
print(f"Max number is {maximum}")



