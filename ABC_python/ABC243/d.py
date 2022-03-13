from collections import deque

N, X = map(int, input().split())
S = list(input())

queue = deque()
for i in bin(X)[2:]:
    queue.append(i)

for s in S:
    if s == "U":
        queue.pop()
    elif s == "L":
        queue.append("0")
    else:
        queue.append("1")

ans = "".join(queue)
print(int(ans, 2))