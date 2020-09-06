name = input("Enter your name: ")
age = int(input(f"Hello {name}, how are you old?: "))
if age < 18:
    print("You are young person")
elif age >= 18 <= 40:
    print("You are middle-aged person")
elif age > 40:
    print("You are old person")
