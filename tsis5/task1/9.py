def count_lines(file_name):
    with open(file_name, 'r') as f:
        txt = f.readlines()
    return len(txt)
print(count_lines('test.txt'))