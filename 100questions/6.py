N = int(input())
S = input()
cnt = 0


for i in range(10):
    if str(i) in S:
        locate_i = S.find(str(i))+1
        s_i = S[locate_i:]
    else:
        continue

    for j in range(10):
        if str(j) in s_i:
            locate_j = s_i.find(str(j))+1
            s_j = s_i[locate_j:]
        else:
            continue

        for k in range(10):
            if str(k) in s_j:
                cnt += 1
            else:
                continue

print(cnt)