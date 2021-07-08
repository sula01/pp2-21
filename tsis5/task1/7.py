def line_by_list(file_name):
    ans = []
    with open(file_name, 'r') as f:
        for line in f: ans.append(line)
    print(ans)

line_by_list('test.txt')