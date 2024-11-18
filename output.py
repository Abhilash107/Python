a = 20
def f():
    a = 10
    b = 10
    def g():
        nonlocal b
        b = b + 2
        print(b)
    g()
    print(a, b)
f()
print(a)