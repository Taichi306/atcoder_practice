N, X, Y = map(int, input().split())

red = [0 for _ in range(10)]
blue = [0 for _ in range(10)]

blue[1] = 1

for i in range(2, N+1):
    blue[i] = red[i-1] + blue[i-1]*Y
    red[i] = red[i-1] + blue[i]*X

print(blue)