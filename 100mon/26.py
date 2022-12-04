from collections import deque

N, Q = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(N-1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    G[a].append(a)
    G[b].append(b)
px = []
for _ in range(Q):
    p, x = map(int, input().split())
    x -= 1
    px.append(p, x)

dp = [0 for _ in range(N)]
