N, M = map(int, input().split())
P = []
Y = []
for _ in range(M):
    p, y = map(int, input().split())
    P.append(p)
    Y.append(y)

YP = list(zip(Y, P, range(M)))
YP.sort()
mark = [1] * (N+1)
ans_list = [[] for _ in range(M)]
for i in range(M):
    up, down = str(YP[i][1]), str(mark[YP[i][1]])
    up_up, down_up = 6-len(up), 6-len(down)
    ans = "0"*up_up + up + "0"*down_up + down
    ans_list[YP[i][2]].append(ans)
    mark[YP[i][1]] += 1

for a in ans_list:
    print(a[0])