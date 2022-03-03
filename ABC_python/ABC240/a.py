a, b = map(int, input().split())
if (a-b) % 10 in [1, 9]:
    print('Yes')
else:
    print('No')