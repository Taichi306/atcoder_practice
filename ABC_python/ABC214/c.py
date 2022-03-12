N = int(input())
S = list(map(int, input().split()))
T = list(map(int, input().split()))

dp = [-1 for _ in range(N)]
dp[0] = T[0]

for i in range(2*N):
    dp[(i+1)%N] = min(dp[i%N]+S[i%N], T[(i+1)%N])

for i in range(N):
    print(dp[i])