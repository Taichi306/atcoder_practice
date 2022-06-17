N, K, X = map(int, input().split())
A = list(map(int, input().split()))

ans = sum(A)
rem = K
Q = sum(x // X for x in A)
R = sorted((x % X for x in A), reverse=True)
ans -= X * min(Q, rem)
rem -= min(Q, rem)
ans -= sum(R[:rem])
print(ans)