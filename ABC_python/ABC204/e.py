from heapq import heappop, heappush

N, M = map(int, input().split())
G = [[] for _ in range(N)]
INF = float('inf')

for _ in range(M):
    A, B, C, D = map(int, input().split())
    A, B = A-1, B-1
    rootD = int(D**0.5)
    G[A].append([B, C, D, rootD])
    G[B].append([A, C, D, rootD])

t = [INF] * N
prev = [-1] * N
t[0] = 0
q = [(0, 0)]

while q:
    cost, A = heappop(q)
    if cost > t[A]:
        continue
    for B, C, D, rootD in G[A]:
        s = rootD - t[A] - 1
        alt = t[A] + C + D // (t[A] + 1)
        if s >= 0:
            alt = min(alt, t[A]+C+s+D//rootD, t[A]+C+1+s+D//(rootD+1))
        if t[B] > alt:
            t[B] = alt
            prev[B] = A
            heappush(q, (alt, B))
x = t[N-1]
if x == INF:
    print('-1')
else:
    print(x)