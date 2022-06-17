import itertools

l1 = ['a', 'b', 'c']
l2 = ['X', 'Y', 'Z']
p = itertools.product(l1, l2)

for i in p:
    print(i)