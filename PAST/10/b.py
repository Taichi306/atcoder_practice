a, b, x, y = map(int, input().split())

cnt = 0

while x > 0 and y > 0:
    x -= a
    y -= b
    cnt += 1

if x < 0 or y < 0:
    cnt -= 1

print(cnt)