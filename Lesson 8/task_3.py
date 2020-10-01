class NewRule(Exception):
    def __init__(self, text):
        self.text = text


string = ''
numbers = []
count = 1
while string != 'q':
    try:
        string = input(f"Enter element №{count} or 'q' for exit: ")
        if not string.lstrip('-').replace('.', '', 1).isdecimal():
            raise NewRule("Entered string, not number")
    except NewRule as err:
        print(err)
    else:
        numbers.append(float(string))
        count += 1

print(numbers)
