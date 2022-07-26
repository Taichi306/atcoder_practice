T, N = map(int, input().split())
test = [0 for _ in range(N)]

for _ in range(T):
    p = tuple(map(int, input().split()))
    for i in range(N):
        if p[i] >= test[i]:
            test[i] = p[i]
    print(sum(test))