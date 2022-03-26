N = int(input())

ans = 0
for i in range(1, N+1, 2):
    yakusu = []
    for j in range(1, N+1):
        if i % j == 0:
            yakusu.append(j)
    if len(yakusu) == 8:
        ans += 1

print(ans)