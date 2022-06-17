N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

ans = 0
for i in range(M):
    for k in range(i+1, M):
        temp = 0
        for j in range(N):
            temp += max(A[j][i], A[j][k])
        ans = max(ans, temp)
print(ans)