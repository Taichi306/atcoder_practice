import sys
sys.setrecursionlimit(10**7)

N = int(input())
edges = [[] for _ in range(N)]
for _ in range(N-1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    edges[a].append(b)
    edges[b].append(a)

for i in range(N):
    edges[i].sort()

ans = []
def dfs(crr, pre):
    ans.append(crr)
    for next in edges[crr]:
        if next != pre:
            dfs(next, crr)
            ans.append(crr)
dfs(0, -1)
ans = map(lambda x: x+1, ans)
print(*ans)