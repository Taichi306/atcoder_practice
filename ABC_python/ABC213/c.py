# できてない
H, W, N = map(int, input().split())
tate = []
yoko = []
for _ in range(N):
    A, B = map(int, input().split())
    tate.append(A)
    yoko.append(B)

x_dict = {}
y_dict = {}

tate = list(set(tate))
yoko = list(set(yoko))
tate.sort()
yoko.sort()

for i, x in enumerate(tate):
    x_dict[x] = i + 1
for i, y in enumerate(yoko):
    y_dict[y] = i + 1

for i in range(N):
    print(x_dict[x[i]], y_dict[y[i]])