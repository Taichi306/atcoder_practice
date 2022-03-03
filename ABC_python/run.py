N = int(input())
AB = [tuple(map(int, input().split())) for _ in range(N)]

from collections import defaultdict
event = defaultdict(int)

for a, b in AB:
    event[a] += 1
    event[a+b] += 1
dl = [0] * (N+1)

pred = 0
cnt = 0

for d in 