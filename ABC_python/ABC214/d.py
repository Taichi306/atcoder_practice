import sys
sys.setrecursionlimit(10**6)

N = int(input())

edges = []

for _ in range(N-1):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    edges.append((w, u, v))
edges.sort()

parents = [-1] * N

def root(x):
    if parents[x] < 0:
        return x
    else:
        parents[x] = root(parents[x])
        return parents[x]

def unite(x, y):
    x = root(x)
    y = root(y)
    parents[x] += parents[y]
    parents[y] = x

def size(x):
    x = root(x)
    return -parents[x]

ans = 0

for w, u, v in edges:
    ans += w * size(u) * size(v)
    unite(u, v)

print(ans)