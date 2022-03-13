#ABC208D
N, M = map(int, input().split())
A, B, C = [], [], []

for _ in range(M):
    a, b, c = map(int, input().split())
    A.append(a)
    B.append(b)
    C.append(c)

INF = 10**18

dp = [[INF]*N for _ in range(N)]
for i in range(N):
    dp[i][i] = 0
for i in range(M):
    a = A[i]-1
    b = B[i]-1
    c = C[i]
    dp[a][b] = c
ans = 0

for k in range(N):
    for i in range(N):
        for j in range(N):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])
            if dp[i][j] < INF:
                ans += dp[i][j]
print(ans)