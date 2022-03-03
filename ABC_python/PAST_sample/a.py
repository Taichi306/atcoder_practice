N, A, B = map(int, input().split())
train = A*N
if train < B:
    print(train)
else:
    print(B)