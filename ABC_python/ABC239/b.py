X = int(input())
 
if X >= 0:
    ans = X // 10
    print(ans)
else:
    ans = X / 10
    if ans == float:
        print(X//10+1)
    else:
        print(X//10)