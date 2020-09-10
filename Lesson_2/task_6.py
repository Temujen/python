size = int(input("Сколько продуктов вы хотите добавить в базу: "))
while size <= 0:
    print("Your enter number <= 0, please try again")
    size = int(input("Сколько продуктов вы хотите добавить в базу: "))

menu = ["Название", "Стоимость", "Количество", "ед."]
result = list()
param = dict()
for i in range(size):
    for j in range(len(menu)):
        param[menu[j]] = input(f"Введите {menu[j]} продукта №{i + 1}: ")
    result.insert(i, (i + 1, param.copy()))
    print()

analytics = {
    "Название": [],
    "Стоимость": [],
    "Количество": [],
    "ед.": []
}
for k in range(len(result)):
    for key, value in result[k][1].items():
        analytics[key].append(value)

for key, value in analytics.items():
    print(key, value)
