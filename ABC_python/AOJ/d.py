N = int(input())
T = list(map(int, input().split()))

dp = [[0]*21 for _ in range(N)]
dp[0][T[0]] = 1

for i in range(1, N-1):
    for j in range(21):
        if ((j + T[i]) <= 20 and dp[i-1][j] >= 1):
            dp[i][j+T[i]] += dp[i-1][j]
        if ((j - T[i]) >= 0 and dp[i-1][j] >=1):
            dp[i][j-T[i]] += dp[i-1][j]

print(dp[N-2][T[-1]])
# print(dp)