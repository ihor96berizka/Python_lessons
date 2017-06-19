def maker(n):
    return lambda x:x ** n

f = maker(2)
print(f(3))
g = maker(3)
print(g(3))
