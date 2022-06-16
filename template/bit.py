"""
x | y : xとyのビット単位 論理和
x ^ y : xとyのビット単位 排他的論理和
x & y : xとyのビット単位 論理積
x << n  xのnビット左シフト
x >> n  xのnビット右シフト
~x    : xのビット反転

ex)
3 << 2 : 3を2ビット左シフト = 12
11 を 1100

"""


product_list = [1, 1, 1]
N = len(product_list)

for i in range(1 << N):
    temp = []
    for j in range(N):
        if i >> j & 1:
            temp.append(1)
            # product_list[j]
        else:
            temp.append(0)
    print(temp)