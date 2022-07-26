N, X, Y, Z = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

people = []

# 数学, 英語, 数学英語合計得, 合格flag, index
for i in range(N):
    people.append([A[i], B[i], A[i]+B[i], False, i+1])

total_n = 0

def check_pass(people, test, test_n, temp_total):
    temp_test = sorted(people, key=lambda x: x[test])
    
    for i in range(test_n):
        if people[temp_test[i][-1]-1][-2] == True:
            pass
        else:
            people[temp_test[i][-1]-1][-2] = True
            temp_total += 1
            if temp_total == N:
                check_tie(temp_test, i)

def check_tie(temp_test):
    all_tie = []
    if temp_test[i] == temp_test[i+1]:
        all_tie.append(i+1)
        check_tie(temp_test, i+1)
    else:
        return all_tie
