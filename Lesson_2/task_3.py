num = int(input("Enter month number: "))
while num <= 0 or num > 12:
    print("Your enter number <= 0, please try again")
    num = int(input("Enter month number: "))
season = {
    "Winter": [12, 1, 2],
    "Spring": [3, 4, 5],
    "Summer": [6, 7, 8],
    "Autumn": [9, 10, 11]
}
for key in season.keys():
    if num in season[key]:
        print(f"This is {key}")