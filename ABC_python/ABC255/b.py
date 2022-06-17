N, K = map(int, input().split())
_A = list(map(int, input().split()))
XY = []
for i in range(N):
    a, b = map(int, input().split())
    XY.append((a, b))

A = []
for i in range(K):
    temp = _A[i] - 1
    A.append(temp)
not_ramp = []
for i in range(N):
    if i not in A:
        not_ramp.append(i)

ans = 0
for i in not_ramp:
    temp1 = XY[i]
    temp_dist = 10**18
    for j in A:
        temp2 = XY[j]
        dist = ((abs(temp1[0]-temp2[0]))**2+ \
        (abs(temp1[1]-temp2[1]))**2)**0.5
        if dist <= temp_dist:
            temp_dist = dist
    if temp_dist >= ans:
        ans = temp_dist
print(ans)