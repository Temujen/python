with open('text_2.txt', 'r', encoding='utf-8') as source_file:
    count_lines = 0
    for line in source_file:
        count_lines += 1
        temp = line.split()
        print(f"String №{count_lines} have {len(temp)} words")
print(f"Total count lines is {count_lines}")
