def f():
    for i in range(2):
        yield i

g = f()
print(next(g))
print(next(g))
print(next(g))