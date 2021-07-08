def file_read(file_name, n_lines):
    from itertools import islice
    with open(file_name) as f:
        for line in islice(f, n_lines):
            print(line)

file_read('test.txt', int(input()))