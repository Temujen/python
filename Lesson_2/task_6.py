info = input("Меню ТОВАРЫ \n"
             + "Для добавления нового товара введите - 1\n"
             + "Для просмотра аналитики введите - 2\n"
             + "Для выхода из программы введите - q\n"
             + "Ваш выбор: ")
menu = ["Название", "Стоимость", "Количество", "ед."]
result = list()
param = dict()
analytics = {
    "Название": [],
    "Стоимость": [],
    "Количество": [],
    "ед.": []
}
count = 0
while info != "q":
    if info == '1':
        print("\n")
        for j in range(len(menu)):
            param[menu[j]] = input(f"Введите {menu[j]} продукта: ")
            result.insert(count, (count + 1, param.copy()))
        for key, value in result[count][1].items():
            analytics[key].append(value)
        count += 1
    elif info == '2':
        if len(result) != 0:
            print("\n")
            for key, value in analytics.items():
                print(key, value)
        else:
            print("\nВы еще не ввели ни одного товара")
    info = input("\nМеню ТОВАРЫ \n"
                 + "Для добавления нового товара введите - 1\n"
                 + "Для просмотра аналитики введите - 2\n"
                 + "Для выхода из программы введите - q\n"
                 + "Ваш выбор: ")
