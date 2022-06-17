# https://atcoder.jp/contests/s8pc-6/tasks/s8pc_6_b


"""
A_iとB_iを経由する, 出口でゴール
1マス1秒


0, 1, 2, 3, 4, 5, 6, 7, 8, 9
   A_i   A_j      B_i   B_j

A = (A_i)+(B_i)... // n
B = (A_j)+...//n

絶対値の合計の最小化は中央値になる
"""

N = int(input())
start, end = [], []
cost = 0

for _ in range(N):
    i, j = map(int, input().split())
    start.append(i)
    end.append(j)
    cost += abs(i-j)

start.sort()
end.sort()

medi_s = start[N//2]
medi_e = end[N//2]

for i in range(N):
    cost += abs(start[i]-medi_s)
    cost += abs(end[i]-medi_e)

print(cost)
