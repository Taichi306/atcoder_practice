from collections import defaultdict

H, W, N = map(int, input().split())
A = []
for _ in range(H):
    a = list(map(int, input().split()))
    A.append(a)
C = list(map(int, input().split()))

dic = defaultdict(set)

def check_right(A, i, j):
    if A[i][j] != A[i][j+1]:
        temp1 = C[A[i][j]-1]
        temp2 = C[A[i][j+1]-1]
        dic[temp1].add(temp2)
        dic[temp2].add(temp1)

def check_donw(A, i, j):
    if A[i][j] != A[i+1][j]:
        temp1 = C[A[i][j]-1]
        temp2 = C[A[i+1][j]-1]
        dic[temp1].add(temp2)
        dic[temp2].add(temp1)

def check_ans(dic):
    dic_keys = list(dic.keys())

    for key in range(len(dic_keys)):
        for i in dic[dic_keys[key]]:
            if i == dic_keys[key]:
                print('No')
                exit()
        for j in dic[dic_keys[key]]:
            if j == dic_keys[key]:
                print('No')
                exit()


if H == 1 and W == 1:
    print('Yes')
    exit()
if H == 1:
    for i in range(1):
        for j in range(W):
            if j == W-1:
                pass
            else:
                check_right(A, i, j)
if W == 1:
    for i in range(H-1):
        for j in range(1):
            check_donw(A, i, j)
else:
    for i in range(H-1):
        for j in range(W):
            if j == W-1:
                check_donw(A, i, j)
            else:
                check_donw(A, i, j)
                check_right(A, i, j)

check_ans(dic)
print('Yes')