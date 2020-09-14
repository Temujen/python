def func_sum(args):
    total = 0
    while True:
        temp = args.split()
        try:
            if "q" in args:
                temp = temp[:temp.index('q')]
                temp = [float(x) for x in temp]
                total += sum(temp)
                return total
            else:
                temp = [float(x) for x in temp]
                total += sum(temp)
                print(f"Interim sum = {total}")
        except ValueError:
            print("Entered wrong symbol, you can enter numbers and 'q', please try again")
        args = input("Enter few number through a space, for exit enter 'q': ")


numbers = input("Enter few number through a space, for exit enter 'q': ")
print(f"Final sum = {func_sum(numbers)}")
