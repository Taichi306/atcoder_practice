N, M = map(int, input().split())
ks = []
for i in range(M):
    _ks = list(map(int, input().split()))
    ks.append(_ks)
p = list(map(int, input().split()))

switches = []
for i in range(1 << N):
    temp = []
    for j in range(N):
        if i >> j & 1:
            temp.append(1)
        else:
            temp.append(0)
    switches.append(temp)

ans = 0
for i in range(len(switches)):
    okay = 0
    for j in range(M):
        cnt = 0
        for k in range(ks[j][0]):
            if switches[i][ks[j][k+1]-1] == 1:
                cnt += 1
        if p[j] % 2 == cnt % 2:
            okay += 1
    if okay == M:
        ans += 1
print(ans)