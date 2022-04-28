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