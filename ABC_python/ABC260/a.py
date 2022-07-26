S = list(input())

if S[0] == S[1] and S[1] == S[2]:
    print(-1)
    exit()

_list1 = []
_list2 = []

for i in range(len(S)):
    if S[i] not in _list1:
        _list1.append(S[i])
    else:
        _list2.append(S[i])

        for j in range(len(_list1)):
            if S[i] == _list1[j]:
                _list1.pop(j)
                break


print(_list1[0])