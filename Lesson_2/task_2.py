num = int(input("Enter list size: "))
while num <= 0:
    print("Your enter number <= 0, please try again")
    num = int(input("Enter list size: "))

source = list()
for x in range(num):
    source.append(input(f"Enter list element №{x+1}: "))
print(f"Source list {source}")
i = 0
while i < (len(source) - 1):
    first = source[i]
    second = source[i + 1]
    source[i] = second
    source[i + 1] = first
    i += 2
print(f"Changed list {source}")