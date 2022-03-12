A, B, C, X = map(int, input().split())
 
if X <= A:
    print(1)
elif A < X <= B:
    prob =  C / (B - A)
    print(prob)
else:
    print(0)