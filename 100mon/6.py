# N = int(input())
# S = input()
# cnt = 0
 
 
# for i in range(10):
#     if str(i) in S:
#         locate_i = S.find(str(i))+1
#         s_i = S[locate_i:]
#     else:
#         continue
 
#     for j in range(10):
#         if str(j) in s_i:
#             locate_j = s_i.find(str(j))+1
#             s_j = s_i[locate_j:]
#         else:
#             continue
 
#         for k in range(10):
#             if str(k) in s_j:
#                 cnt += 1
#             else:
#                 continue
 
# print(cnt)



N = int(input())
S = list(map(int, input()))

hyaku, zyu, ichi = [], [], []
cnt = 0

for i in range(N-2):
    if S[i] not in hyaku:
        hyaku.append(S[i])
    else:
        continue

    for j in range(i+1, N-1):
        if S[j] not in zyu:
            zyu.append(S[j])
        else:
            continue

        for k in range(j+1, N):
            if S[k] not in ichi:
                ichi.append(S[k])
                cnt += 1
            else:
                continue
        ichi = []
    zyu = []

print(cnt)