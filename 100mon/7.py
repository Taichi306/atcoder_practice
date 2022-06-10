n = int(input())
xy = [tuple(map(int, input().split())) for _ in range(n)]
ste_xy = set(xy)
ans = 0

for i in range(n):
    x1, y1 = xy[i]
    for j in range(i+1, n):
        x2, y2 = xy[j]
        vecx, vecy = x2-x1, y2-y1
        if 