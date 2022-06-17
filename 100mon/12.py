N, M = map(int, input().split())
people = [[0]*N for _ in range(N)]

for _ in range(M):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    people[x][y] = 1
    people[y][x] = 1


patterns = []
for i in range(1<<N):
    temp =[]
    for j in range(N):
        if i >> j & 1:
            temp.append(1)
        else:
            temp.append(0)
    patterns.append(temp)


