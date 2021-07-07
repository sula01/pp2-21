def text_read(file_name):
    txt = open(file_name)
    print(txt.read())

text_read('test.txt')