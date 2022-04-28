import itertools

l1 = ['a', 'b', 'c']
l2 = ['X', 'Y', 'Z']

p = itertools.product(l1, l2)
print(p)

for i in p:
    print(i)