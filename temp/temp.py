N = int(input())
Graph = [[] for _ in range(N)]
for _ in range(N-1):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    Graph[u].append(v)
    Graph[v].append(u)

print(Graph)