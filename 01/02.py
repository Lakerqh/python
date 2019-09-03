a = list(range(1,11))
print(a)
l = []
for x in range(1,11):
    l.append(x * x)
print(l)

j = [x * x for x in range(1,11)]
print(j)

d = {'jack':10,'lily':20,'tom':23}
for k, v in d.items():
    print(k,v)

g = (x * x for x in range(10))
print(g)
print(next(g))
print(next(g))
for x in g:
    print(x)

def add(x, y ,f):
    return f(x) + f(y)
s = add(-1, 4, abs)
print(s)