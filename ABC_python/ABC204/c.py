from collections import deque
import collections

N, M = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(M)]

if M == 0:
    print(N)
    exit()

G = [[] for _ in range(N)]
for i in range(M):
    G[AB[i][0]-1].append(AB[i][1]-1)


def bfs(start):
    count = 1
    mark = [False] * (N)
    mark[start] = True
    q = deque()
    q.append(start)

    while q:
        v = q.popleft()
        for i in G[v]:
            if mark[i] != False:
                continue
            mark[i] = True
            q.append(i)
    count = collections.Counter(mark)
    return count[True]

ans = 0

for i in range(N):
    count = bfs(i)
    ans += count

print(ans)