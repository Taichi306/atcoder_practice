S = list(input())
moji = ["A","C","G","T"]

ans = 0
cnt = 0
for i in S:
    if i in moji:
        cnt += 1
    else:
        if cnt >= ans:
            ans = cnt
        cnt = 0

ans = max(cnt, ans)
print(ans)