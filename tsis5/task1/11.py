import os
def file_size_read(file_name):
    inf = os.stat(file_name)
    return inf.st_size

print("File size in bytes of a plain file:", file_size_read('test.txt'))