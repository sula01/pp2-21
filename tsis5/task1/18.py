def word_count(file_name):
    with open(file_name) as file:
        data = file.read()
        data.replace(',', ' ')
        return len(data.split(' '))

print(word_count('words.txt'))