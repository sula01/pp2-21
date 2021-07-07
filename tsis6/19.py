def test(a):
        def add(b):
                nonlocal a
                a += 1
                return a + b
        return add
n = int(input())
func= test(n)
print(func(n))