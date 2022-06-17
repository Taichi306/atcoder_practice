N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)] 

score = 0

pairs = []

for j in range(M):
    for k in range(j+1, M):
        pairs.append((j, k))

for pair_j, pair_k in pairs:
    temp = 0
    for i in range(N):
        temp += max(A[i][pair_j], A[i][pair_k])
    score = max(score, temp)
print(score)