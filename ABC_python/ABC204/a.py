x, y = map(int, input().split())
if x == y:
    print(x)
else:
    a = [0, 1, 2]
    a.remove(x)
    a.remove(y)
    print(a[0])

x, y = map(int, input().split())

temp = 3

if x != y:
    print(temp-x-y)
else:
    print(x)