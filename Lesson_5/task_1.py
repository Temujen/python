with open('task_1.txt', 'w', encoding='utf-8') as result_file:
    string = input("Enter string or for exit enter null string: ")
    while string != '':
        print(string, file=result_file)
        string = input("Enter string or for exit enter null string: ")
