import heapq

N, M = map(int, input().split())
temp = [list(map(int, input().split())) for _ in range(M)]
G = [[] for _ in range(N)]
for i in range(M):
    G[temp[i][0]].append([temp[i][1], temp[i][2]])


def dijkstra(N, G, start):
    dist = [-1 for _ in range(N)]
    Q = []
    # 始点となる0をヒープに追加 & (頂点, 距離)となるように追加)
    heapq.heappush(Q, [start, 0])
    dist[start] = 0

    # ヒープから取り出したことがあるかを確認する配列
    done = [False for _ in range(N)]

    while len(Q):
        i, d = heapq.heappop(Q)
        if done[i]:
            continue
        for j, c in G[i]:
            if dist[j] == -1 or dist[j] > dist[i] + c:
                dist[j] = dist[i] + c
                heapq.heappush(Q, [j, dist[j]])

    return dist

ans = dijkstra(N, G, 0)
print(ans[-1])