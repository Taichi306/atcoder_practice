N = int(input())
YX = []
ydict = {}
for i in range(N):
    x, y = map(int, input().split())
    if y not in ydict:
        ydict[y] = []
    ydict[y].append((x, i))
 
S = list(input())

for i in ydict:
    value = ydict[i]
    if len(value) >= 2:
        value.sort()
        temp = []
        for j in value:
            temp.append(S[j[1]])
        R_left = -1
        for k in range(len(temp)):
            if temp[k] == 'R':
                R_left = k
            if temp[k] == "L" and R_left >=0 and k >= R_left:
                print('Yes')
                exit()
print('No')

# ----------------------------------------------------------------
N = int(input())

row = {}

for i in range(N):
    x, y = map(int, input().split())
    if y not in row:
        row[y] = []
    row[y].append((x, i))

S = list(input())

INF = 10**18

for y, people in row.items():
    Rmin = INF
    Lmax = -INF
    
    for x, i in people:
        if S[i] == "R":
            Rmin = min(Rmin, x)
        elif S[i] == "L":
            Lmax = max(Lmax, x)
    if Rmin <= Lmax:
        print('Yes')
        exit()
print('No')

# -------------------------------------------------------------------------
N = int(input())

row = {}

for i in range(N):
    x, y = map(int, input().split())
    if y not in row:
        row[y] = []
    row[y].append((x, i))
S = list(input())

INF = 10**18

for people in row.values():
    if len(people) >= 2:
        Rmin = INF
        Lmax = -INF
        for x, i in people:
            if S[i] == "R":
                Rmin = min(Rmin, x)
            elif S[i] == "L":
                Lmax = max(Lmax, x)
        if Rmin <= Lmax:
            print('Yes')
            exit()
print('No')