from collections import defaultdict


class UnionFind:
    def __init__(self, N):
        self.n = N
        self.parents = [-1] * (N+10)
        self.group = defaultdict(set)
    
    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]
    
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return
        if self.parents[x] > self.parents[y]:
            x, y = y, x
        self.parents[x] += self.parents[y]
        self.parents[y] = x

        if self.group[y]:
            for each in self.group[y]:
                self.group[x].add(each)
        self.group[x].add(y)
        self.group.pop(y)
    
    def show_member_including_root(self, x):
        root = self.find(x)
        members = list(self.group[root])
        members += [root]

        return members
    
    def size(self, x):
        # 要素xが属するグループのサイズを返す
        return -self.parents[self.find(x)]
    
    
    

N, Q = map(int, input().split())
uf = UnionFind(N)

queries = []

for _ in range(Q):
    q = list(map(int, input().split()))
    queries.append(q)

for query in queries:
    if query[0] == 1:
        uf.union(query[1], query[2])
    else:
        ans = uf.show_member_including_root(query[1])
        ans.sort()
        print(*ans)