def int_func(args):
    while True:
        err = 0
        for el in args:
            if (ord(el) < 97 or ord(el) > 122) and ord(el) != 32:
                err += 1
        if err > 0:
            print("Entered wrong symbol, try again")
            args = input("Enter latin words in lower case: ")
        else:
            return args.title()


word = input("Enter latin words in lower case: ")
print(int_func(word))
