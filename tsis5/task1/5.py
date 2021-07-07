def file_to_list(file_name):
    with open(file_name) as f:
        list = f.readlines()
        print(list)

file_to_list('test.txt')