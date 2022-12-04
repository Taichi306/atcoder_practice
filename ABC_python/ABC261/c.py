from collections import defaultdict

dic = defaultdict(int)

N = int(input())
S = []
for _ in range(N):
    s = str(input())
    S.append(s)

for i in range(N):
    dic[S[i]] += 1
    if dic[S[i]] > 1:
        print(S[i] + f"({dic[S[i]]-1})")
    else:
        print(S[i])