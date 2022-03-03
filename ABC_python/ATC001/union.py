class UnionFind:
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n
    
    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]
    
    def merge(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return 
        if self.parents[x] > self.parents[y]:
            x, y = y, x
            self.parents[x] += self.parents[y]
            self.parents[y] = x
    
    def same(self, x, y):
        return self.find(x) == self.find(y)
        
union = UnionFind(10**6)
N, Q = map(int, input().split())
for _ in range(Q):
    p, a, b = map(int, input().split())
    if p == 0:
        union.merge(a, b)
    else:
        if union.same(a, b):
            print('Yes')
        else:
            print('No')