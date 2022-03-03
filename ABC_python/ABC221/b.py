S = str(input())
T = str(input())

if S == T:
    print('Yes')
    exit()

mark = [0] * len(S)

for i in range(len(S)):
    if S[i] != T[i]:
        mark[i] = 1

ng = 0
index = []
for i in range(len(S)):
    if mark[i] == 1:
        ng += 1
        index.append(i)

if ng > 2  or ng == 1:
    print('No')
elif abs(index[0]-index[1]) == 1 and S[index[0]] == T[index[1]] and S[index[1]] == T[index[0]]:
    print('Yes')
else:
    print('No')


##---------------------------------------------------------------
s = list(input())
t = list(input())
if s == t:
    print('Yes')
    exit()

for i in range(len(s)-1):
    s[i], s[i+1] = s[i+1], s[i]
    if s == t:
        print('Yes')
        exit()
    s[i], s[i+1] = s[i+1], s[i]
print('No')