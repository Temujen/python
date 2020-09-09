string = input("Enter string: ")
result = string.split()
for num, el in enumerate(result):
    if len(el) > 10:
        el = el[:10]
        print(num + 1, el)
    else:
        print(num + 1, el)
