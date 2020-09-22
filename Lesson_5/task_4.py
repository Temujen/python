def check_words(string):
    dictionary = {'One': "Один", 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
    for key, value in dictionary.items():
        if string == key:
            return value


with open('text_4.txt', 'r', encoding='utf-8') as source_file:
    with open('text_4_dest.txt', 'w', encoding='utf-8') as result_file:
        for line in source_file:
            word, number = line.split(' - ')
            word_translate = check_words(word)
            result_file.write(f"{word_translate} - {number}")
