A, B, C, X, Y = map(int, input().split())

ans = 10**10

for i in range(10**5+1):
    ans = min(ans, A*max(X-i, 0) + B*max(Y-i, 0) + 2*C*i)
print(ans)

# -----------------------------------------------------------------
A, B, C, X, Y = map(int, input().split())

ans = 10**10

for i in range(max(X, Y)+1):
    ans = min(ans, A*max(X-i, 0) + B*max(Y-i, 0) + 2*C*i)
print(ans)