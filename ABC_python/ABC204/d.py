N = int(input())
T = [0] + list(map(int, input().split()))

sum_T = sum(T)

dp = [[False]*(sum_T+1) for _ in range(N+1)]
dp[0][0] = True

for i in range(1, N+1):
    for j in range(sum_T+1):
        if dp[i-1][j] == True:
            dp[i][j] = True
        if dp[i-1][j-T[i]] == True and 0 <= j - T[i]:
            dp[i][j] = True

ans = 10**20

for i in range(sum_T+1):
    if dp[N][i] == True:
        ans = min(ans, max(i, sum_T-i))
print(ans)