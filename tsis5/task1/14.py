with open('abc.txt') as file1, open ('test.txt') as file2:
    for l1, l2 in zip(file1, file2):
        print(l1 + l2)
