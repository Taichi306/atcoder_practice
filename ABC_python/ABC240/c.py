N, X = map(int, input().split())
a = [0] + []
b = [0] + []
for _ in range(N):
    A, B = map(int, input().split())
    a.append(A)
    b.append(B)

dp = [[False for _ in range(X+1)] for _ in range(N+1)]
dp[0][0] = True

for i in range(1, N+1):
    for j in range(X+1):
        if dp[i-1][j] == True and j + a[i] <= X:
            dp[i][j+a[i]] = True
        if dp[i-1][j] == True and j + b[i] <= X:
            dp[i][j+b[i]] = True
   
if dp[N][X]:
    print('Yes')
else:
    print('No')