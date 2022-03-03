N = int(input())
A = list(map(int, input().split()))
B = A.copy()

A.sort()

for i in range(N):
    if B[i] == A[-2]:
        i += 1
        print(i)