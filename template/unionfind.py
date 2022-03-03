from collections import defaultdict

class UnionFind():
    def __init__(self, n):
        self.n = n
        # parentsは各要素の親要素の番号を格納するリスト
        self.parents = [-1] * n
    
    def find(self, x):
        # 要素xが属するグループの根を返す
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]
    
    def union(self, x, y):
        # 要素xが属するグループと要素yが属するグループとを併合する
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return 
        if self.parents[x] > self.parents[y]:
            x, y = y, x
        # parents[x]にyを併合
        self.parents[x] += self.parents[y]
        # parents[y]の根をxに更新
        self.parents[y] = x
    
    def size(self, x):
        # 要素xが属するグループのサイズを返す
        return -self.parents[self.find(x)]
    
    def same(self, x, y):
        # Trueなら根が同じ
        return self.find(x) == self.find(y)
    
    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]
    
    def roots(self):
        # すべての根の要素をリストで返す
        return [i for i, x in enumerate(self.parents) if x < 0]
    
    def group_count(self):
        return len(self.roots())
    
    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

