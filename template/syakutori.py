###ABC130D###

N, K = map(int, input().split())
A = list(map(int, input().split()))

left = 0
total = 0
ans = 0

for right in range(0, N):
    total += A[right]
    while total >= K:
        ans += N - right
        total -= A[left]
        left += 1
print(ans)