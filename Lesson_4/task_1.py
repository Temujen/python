from sys import argv

name, work, rate, prize = argv


def profit(work, rate, prize):
    try:
        result = float(work) * float(rate) + float(prize)
        if result > 0:
            return round(result, 3)
        else:
            print("Please enter only positive number, try again")
            return
    except ValueError:
        print("Please enter only 3 positive number, try again")


print(f"Your profit is {profit(work, rate, prize)}")
