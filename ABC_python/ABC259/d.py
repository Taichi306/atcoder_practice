from collections import defaultdict

class UnionFind:
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n
        self.group_members = defaultdict(list)
    
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

        if self.group_members[y]:
            for i in self.group_members[y]:
                self.group_members[x].append(i)
        self.group_members[x].append(y)
        self.group_members.pop(y)
    
    def members(self, x):
        root = self.find(x)
        members = self.group_members[root] + [root]
        return members
    
    def same(self, x, y):
        # Trueなら根が同じ
        return self.find(x) == self.find(y)


def check_if_has_kouten(xyr_1, xyr_2):
    dist = (abs(xyr_1[0] - xyr_2[0]))**2 + (abs(xyr_1[1] - xyr_2[1]))**2

    if dist == (xyr_1[2]+xyr_2[2])**2:
        return True
    if (xyr_1[2]-xyr_2[2])**2 < dist < (xyr_1[2]+xyr_2[2])**2:
        return True
    if dist == (xyr_1[2]-xyr_2[2])**2:
        return True
    return False

N = int(input())
s_x, s_y, t_x, t_y = map(int, input().split())
xyr = []
for i in range(N):
    x, y, r = map(int, input().split())
    xyr.append((x, y, r))


uf = UnionFind(N+1)

flag_s = -1
flag_t = -1

for i in range(N):
    for j in range(i+1, N):
        if check_if_has_kouten(xyr[i], xyr[j]):
            uf.union(i, j)
    if flag_s < 0:
        if (xyr[i][0] + xyr[i][2], xyr[i][1]) == (s_x, s_y):
            flag_s = i
        if (xyr[i][0] - xyr[i][2], xyr[i][1]) == (s_x, s_y):
            flag_s = i
        if (xyr[i][0], xyr[i][1]+xyr[i][2]) == (s_x, s_y):
            flag_s = i
        if (xyr[i][0], xyr[i][1]-xyr[i][2]) == (s_x, s_y):
            flag_s = i
    if flag_t < 0:
        if (xyr[i][0] + xyr[i][2], xyr[i][1]) == (t_x, t_y):
            flag_t = i
        if (xyr[i][0] - xyr[i][2], xyr[i][1]) == (t_x, t_y):
            flag_t = i
        if (xyr[i][0], xyr[i][1]+xyr[i][2]) == (t_x, t_y):
            flag_t = i
        if (xyr[i][0], xyr[i][1]-xyr[i][2]) == (t_x, t_y):
            flag_t = i

if flag_s < 0 or flag_t < 0:
    print('No')
    exit()

if uf.same(flag_s, flag_t):
    print('Yes')
else:
    print('No')

