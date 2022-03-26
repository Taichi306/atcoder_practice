while True:
    count = 0
    n, x = map(int, input().split())
    if n == 0 and x == 0:
        break
    for i in range(1, n+1):
        for j in range(i, n+1):
            for k in range(j, n+1):
                if i + j + k == x and i != j and j != k and k != i:
                    count += 1
    print(count)
exit()