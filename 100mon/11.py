"""
switchのon/offを1/0としてbit探索して, pと整合性が取れかつ
電球が全て点灯してればいい?
"""

N, M = map(int, input().split())
ks = []
for _ in range(M):
    temp = list(map(int, input().split()))
    ks.append(temp)
p = list(map(int, input().split()))


patterns = []

for i in range(1<<N):
    temp = []
    for j in range(N):
        if i >> j & 1:
            temp.append(1)
        else:
            temp.append(0)
    patterns.append(temp)

ans = 0
for pattern in patterns:
    on_n_lamp = []    
    for i in range(len(ks)):
        temp = 0
        for j in range(1, len(ks[i])):
            if pattern[ks[i][j]-1] == 1:
                temp += 1
        on_n_lamp.append(temp)
    okay = 0
    for k in range(len(p)):
        if on_n_lamp[k]%2 == p[k]:
            okay += 1
    if okay == M:
        ans += 1

print(ans)