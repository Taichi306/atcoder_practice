N = int(input())
s = [input() for _ in range(N)]

ans = 0
M = {}

for x in s:
    x = "".join(sorted(x))
    if x not in M:
        M[x] = 0
    M[x] += 1

for x in M.values():
    ans += x*(x-1)//2
print(ans)