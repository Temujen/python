def check_numbers(argv):
    while True:
        temp = argv.split()
        try:
            temp = [float(x) for x in temp]
            return argv, sum(temp)
        except ValueError:
            print(mes_alert)
            argv = input(message)


message = "Enter number through space, for exit enter null string: "
mes_alert = "You enter wrong string, please try again"
summary = 0
with open('text_5.txt', 'w', encoding='utf-8') as result_file:
    string = input(message)
    while string != '':
        string, sum_line = check_numbers(string)
        summary += sum_line
        if string != '':
            print(string, file=result_file)
            string = input(message)
print(f"Total summary is {summary}")
