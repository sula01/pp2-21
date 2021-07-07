def read_lines(file_name):
    with open(file_name, 'r') as f:
        print(f.readlines())

read_lines('test.txt')