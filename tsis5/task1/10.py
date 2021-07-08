from collections import Counter
def word_count(file_name):
    with open(file_name, 'r') as f:
        return Counter(f.read().split())

print('Number of words:', word_count('test.txt'))