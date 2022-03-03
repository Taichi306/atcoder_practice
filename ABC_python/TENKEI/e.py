import heapq

N, M = map(int, input().split())
temp = [list(map(int, input().split())) for _ in range(M)]
G = [[] for _ in range(N)]
for i in range(M):
    G[temp[i][0]].append([temp[i][1], temp[i][2]])

def dijkstra(start):
    dist = [-1 for _ in range(N)]
    Q = []
    heapq.heappush(Q, [start, 0])
    dist[start] = 0
    done = [False for _ in range(N)]
    while len(Q):
        i, d = heapq.heappop(Q)
        if done[i]:
            continue
        for j, c in G[i]:
            if dist[j] == -1 or dist[j] > dist[i] + c:
                dist[j] = dist[i] + c

                heapq.heappush(Q, [j, dist[j]])
    count = 0
    for i in range(N):
        if dist[i] != -1:
            count += dist[i]

    return count
    
ans = 0
for i in range(N):
    count = dijkstra(i)
    ans += count

print(ans)
