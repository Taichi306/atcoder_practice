L1, R1, L2, R2 = map(int, input().split())

# L1, R1, L2, R2 = 0, 3, 1, 5

if R1 <= L2:
    print(0)
elif R2 <= L1:
    print(0)
elif L2 <= R1:
    print(R1-L2)
elif L1 == L2 and R1 == R2:
    print(R1-L1)
else:
    print(L1-R2)
