num = int(input("Enter month number: "))
while num <= 0 or num > 12:
    print("Your enter number <= 0, please try again")
    num = int(input("Enter month number: "))
season = [
    {12: "Winter"}, {1: "Winter"}, {2: "Winter"},
    {3: "Spring"}, {4: "Spring"}, {5: "Spring"},
    {6: "Summer"}, {7: "Summer"}, {8: "Summer"},
    {9: "Autumn"}, {10: "Autumn"}, {11: "Autumn"}
]
for i in range(len(season)):
    if num in season[i].keys():
        test = str(season[i].get(num))
        print(f"This is {test}")
