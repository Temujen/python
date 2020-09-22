result = {}
with open('text_6.txt', 'r', encoding='utf-8') as source_file:
    for line in source_file:
        theme, info = line.split(":")
        marks = info.split()
        marks = [int(x[:x.find('(')]) for x in marks if x != '-']
        result[theme] = sum(marks)
print(result)
