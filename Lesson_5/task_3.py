with open('text_3.txt', 'r', encoding='utf-8') as source_file:
    check = 20000
    count = 0
    summurize = 0
    for line in source_file:
        surname, salary = line.split()
        count += 1
        summurize += float(salary)
        if float(salary) < check:
            print(f"{surname} {salary}")
    print(f"Average salary is {summurize / count}")
