N = int(input())
A = []
for _ in range(N):
    a = list(map(str, input()))
    A.append(a)


for i in range(N):
    for j in range(N):
        if i == j:
            continue
        if A[i][j] == "W" and not A[j][i] == "L":
            print("incorrect")
            exit()
        if A[i][j] == "D" and not A[j][i] == "D":
            print("incorrect")
            exit()
        
print('correct')
