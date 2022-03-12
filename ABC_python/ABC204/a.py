x, y = map(int, input().split())
if x == y:
    print(x)
else:
    a = [0, 1, 2]
    a.remove(x)
    a.remove(y)
    print(a[0])