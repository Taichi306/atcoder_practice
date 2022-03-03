import numpy as np

N = int(input())
A = list(map(int, input().split()))
a, cnt = np.unique(A, return_counts=True)

ans = 0
for i in cnt:
    ans += i * (N-i)
print(ans//2)