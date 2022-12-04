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

 
def dfs(i) :
  for v in graph[i] :
    if not visited[v] :
      visited[v] = True
      dfs(v)
      
n , m = map(int,input().split())
 
graph = [[] for i in range(n + 1)]
 
for i in range(m) :
  a , b = map(int,input().split())
  graph[a].append(b)
  
ans = 0
 
for i in range(1 , n + 1) :
  visited = [False] * (n + 1)
  visited[i] = True
  dfs(i)
  ans += visited.count(True)
  
print(ans)