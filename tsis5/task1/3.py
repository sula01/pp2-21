def file_append(file_name):
    from itertools import islice
    with open('abc.txt', 'w') as f:
        f.write('Sultanbek Agabek\n')
        f.write('KBTU, FIT\n')
        f.write('Kak dela bro\n')
        f.write('Hello World')
    txt = open(file_name)
    print(txt.read())

file_append('abc.txt')