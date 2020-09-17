from itertools import count, cycle, islice
from sys import argv

name, start_number, symbols = argv
try:
    print(f"Start number is {int(start_number)}")
    for i in islice(count(int(start_number)), 5):
        print(i)
    print(f"Repeat symbols is {symbols}")
    for j in islice(cycle(symbols), 2 * len(symbols)):
        print(j)
except ValueError:
    print("Enter integer number and any string, example: 2 HELLO")
