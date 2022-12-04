S = input()
T = input()

S += "#"
T += "#"


def assyuku(mojiretsu):
    S_list = []
    start = mojiretsu[0]
    cnt = 1
    for i in range(1, len(mojiretsu)):
        if mojiretsu[i] != start:
            S_list.append((mojiretsu[i-1], cnt))
            cnt = 1
            start = mojiretsu[i]
        else:
            cnt += 1
    return S_list

S_list = assyuku(S)
T_list = assyuku(T)

if len(S_list) != len(T_list):
    print('No')
    exit()


for i in range(len(T_list)):
    if S_list[i][0] != T_list[i][0]:
        print('No')
        exit()
    if S_list[i][1] > T_list[i][1]:
        print('No')
        exit()
    if S_list[i][1] == 1 and T_list[i][1] > 1:
        print('No')
        exit()
print('Yes')