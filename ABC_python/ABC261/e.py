N, C = map(int, input().split())
TA = []
for _ in range(N):
    t, a = map(int, input().split())
    TA.append((t, a))

print('begin-----------------------------')



for i in range(N):
    if TA[i][0] == 1:
        C = C & TA[i][1]
    if TA[i][0] == 2:
        C = C | TA[i][1]
    if TA[i][0] == 3:
        C = C ^ TA[i][1]
    print(C)