A, B = map(int, input().split())

if A == B:
    print(1)
    exit()
else:
    power = abs(A - B)
    ans = 1
    for i in range(power):
        ans *= 32
    print(ans)

#-------------------------------------------
print(32**(A-B))