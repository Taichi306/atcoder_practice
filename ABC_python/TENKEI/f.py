import heapq
 
N,M = map(int, input().split())
 
G = [[] for _ in range(N)]
for _ in range(M):
    u,v,c = map(int, input().split())
    G[u].append((v,c))
    G[v].append((u,c))
 
visited = [False for _ in range(N)]
visited[0] = True
 
Q = []
heapq.heapify(Q)

for j,c in G[0]:
    heapq.heappush(Q, (c,j))
 
res = 0
while len(Q) > 0:
    c,i = heapq.heappop(Q)
    
    if visited[i]:
        continue
    visited[i] = True
    res += c
    
    for (j,c) in G[i]:
        if visited[j]:
            continue
        heapq.heappush(Q, (c,j))
 
print(res)