class NewRule(Exception):
    def __init__(self, text):
        self.text = text


try:
    number_1 = float(input("Enter first number: "))
    number_2 = float(input("Enter first number: "))
    if number_2 == 0:
        raise NewRule('My exception, Warning - division by zero')
except (ValueError, NewRule) as err:
    print(err)
else:
    print(round(number_1 / number_2, 3))
