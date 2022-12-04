N, X = map(int, input().split())
a = [0] + []
b = [0] + []
for _ in range(N):
    A, B = map(int, input().split())
    a.append(A)
    b.append(B)

dp = [[False for _ in range(X+1)] for _ in range(N+1)]
dp[0][0] = True

for i in range(1, N+1):
    for j in range(X+1):
        if dp[i-1][j] == True and j + a[i] <= X:
            dp[i][j+a[i]] = True
        if dp[i-1][j] == True and j + b[i] <= X:
            dp[i][j+b[i]] = True
   
if dp[N][X]:
    print('Yes')
else:
    print('No')


#---------------------------------------------------------
N, X = map(int, input().split())
AB = []
for i in range(N):
    a, b = map(int, input().split())
    AB.append((a, b))


dp = [-1 for _ in range(X+1)]

def find_index(dp, num):
    index_list = []
    for i in range(len(dp)):
        if dp[i] == num:
            index_list.append(i)
    return index_list

for i in range(len(AB)):
    if i == 0:
        if not(len(dp) <= AB[i][0]):
            dp[AB[i][0]] = i
        if not(len(dp) <= AB[i][1]):
            dp[AB[i][1]] = i
    else:
        index_list = find_index(dp, i-1)
        for index in index_list:
            if index+AB[i][0] <= X:
                dp[index+AB[i][0]] = i
            if index+AB[i][1] <= X:
                dp[index+AB[i][1]] = i

if dp[-1] == len(AB)-1:
    print('Yes')
else:
    print("No")