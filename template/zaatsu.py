###ABC36C###
N = int(input())
A = [int(input()) for _ in range(N)]

print(A)

D = { v:i for i, v in enumerate(sorted(set(A)))}
print(D)

for a in A:
    print(D[a])

###ABC213C###
H, W, N = map(int, input().split())
A = []
B = []
for _ in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

D_x = { v:i for i, v in enumerate(sorted(set(A)))}
D_y = { v:i for i, v in enumerate(sorted(set(B)))}

for i in range(N):
    print(D_x[A[i]]+1, D_y[B[i]]+1)