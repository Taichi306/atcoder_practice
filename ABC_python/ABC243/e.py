N, M = map(int, input().split())
INF = 10**18
dp = [[INF]*N for _ in range(N)]
edges = []

for _ in range(M):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    dp[a][b] = c
    dp[b][a] = c
    edges.append((a, b, c))

for k in range(N):
    for i in range(N):
        for j in range(N):
            dp[i][j] = min(dp[i][j], dp[i][k]+dp[k][j])

ans = 0

for a, b, c in edges:
    unused = 0
    for i in range(N):
        if dp[a][i] + dp[i][b] <= c:
            unused = 1
    ans += unused
print(ans)
