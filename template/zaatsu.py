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


# 2つの円が交点を持つ
def check_if_has_kouten(xyr_1, xyr_2):
    dist = (abs(xyr_1[0] - xyr_2[0]))**2 + (abs(xyr_1[1] - xyr_2[1]))**2
    # 外接
    if dist == (xyr_1[2]+xyr_2[2])**2:
        return True
    # 2点の交点
    if (xyr_1[2]-xyr_2[2])**2 < dist < (xyr_1[2]+xyr_2[2])**2:
        return True
    # 内接
    if dist == (xyr_1[2]-xyr_2[2])**2:
        return True
    
    return False