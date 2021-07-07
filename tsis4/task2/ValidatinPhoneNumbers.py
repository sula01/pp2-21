import re
n = int(input())
for i in range(n):
    x = input()
    if bool(re.search(r'^[789][0-9]{9}$', x)):
         print('YES')
    else:
         print('NO')