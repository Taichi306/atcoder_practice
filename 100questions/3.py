S = list(input())
temp = ['A', "C", "G", "T"]

count = 0
ans = -10
for i in range(len(S)):
    if S[i] in temp:
        count += 1
    else:
        ans = max(ans, count)
        count = 0
print(max(count, ans))