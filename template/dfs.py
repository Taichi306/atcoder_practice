import sys
sys.setrecursionlimit(10**7)

N = int(input())
G = [[] for _ in range(N)]
for _ in range(N-1):
    A, B = map(int, input().split())
    A -= 1
    B -= 1
    G[A].append(B)
    G[B].append(A)

for i in range(N):
    G[i].sort()

ans = []
def dfs(crr, pre):
    ans.append(crr)
    for next in G[crr]:
        if next != pre:
            dfs(next, crr)
            ans.append(crr) # 帰ってきたときのやつ

dfs(0, -1)
ans = map(lambda x: x+1, ans)
print(*ans)