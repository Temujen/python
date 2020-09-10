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

# for x in range(len(result)):
#     print(result[x])
# result = [
#     (1, {'Название': 'молоко', 'Стоимость': '50', 'Количество': '2', 'ед.': 'бут.'}),
#     (2, {'Название': 'хлеб', 'Стоимость': '20', 'Количество': '1', 'ед.': 'шт.'})
# ]
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
