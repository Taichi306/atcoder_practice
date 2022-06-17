X, A, D, N = map(int, input().split())

"""
初項, A
交差, D
項数, N
等差数列, S

S_n = A + D*N (N=0, 1, 2, 3...)

・Xが初項より小さい = abs(S_1 - X)
・Xが末項より大きい = abs(S_n - X)
・等差数列を2分探索して, 一番近い数字との差を調べる

A = A + D * (N-1)

"""
n = N
n //= 2
middle = A + D * n

left = 0
right = N

while abs(middle - X) >= D:
    if middle > X:
        right = N//2
    else:
        left = N//2

print(right)
print(left)