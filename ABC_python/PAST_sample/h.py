from heapq import heappush, heappop, heapify

N, M = map(int, input().split())
A = list(map(int, input().split()))

A = [-a for a in A]
heapify(A)

for _ in range(M):
    a = -heappop(A)
    a //= 2
    heappush(A, -a)
print(sum(-a for a in A))