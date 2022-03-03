N, T = map(int, input().split())
c = []
t = []
for _ in range(N):
    _c, _t = map(int, input().split())
    c.append(_c)
    t.append(_t)
 
max = 10000
for i in range(N):
    if t[i] <= T and max >= c[i]:
        max = c[i]
 
if max == 10000:
    print('TLE')
    exit()
 
print(max)