N = int(input())
zero = 0

def gcd(x, y):
    return 1
for _ in range(N):
    x, y = map(int, input().split())
    if (x == 0 and y == 0):
        zero += 1
        continue
    g = gcd(x, y)
    x /= g
    y /= g
    if (y < 0):
        x = -x
        y = -y
    if (y == 0 and x < 0):
        x = -x
        y = -y
    