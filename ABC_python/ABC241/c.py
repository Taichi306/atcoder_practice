N = int(input())
S = [input() for _ in range(N)]

dxs = [1, 1, 0, -1]
dys = [0, 1, 1, 1]


for i in range(N):
    for j in range(N):
        for d in range(4):
            dx = dxs[d]
            dy = dys[d]
            white = 0
            for k in range(6):
                nx = j + dx * k
                ny = i + dy * k

                if not(0<= nx < N and 0<= ny < N):
                    white = 100
                    break
                if S[ny][nx] == '.':
                    white += 1
            
            if white <= 2:
                print('Yes')
                exit()
print('No')


# ---------------------------------------------
def solve():
    def judge(sr, sc, dr, dc):
        """始点(sr, sc) 移動方向(dr, dc)"""
        row, col = sr, sc
        bl = 0
        for _ in range(6):
            if not (0 <= row < N and 0 <= col < N):  # 6マス取り出す前にマスからはみ出すので判定しない
                return False
            bl += S[row][col]
            row += dr
            col += dc
        return bl >= 4

    pat = [(1, 0), (0, 1), (1, -1), (1, 1)]  # 下、右、左下、右下
    N = int(input())
    S = [[1 if c == "#" else 0 for c in input()] for _ in range(N)]  # "#"を1, "."を0に変換します
    for row in range(N):
        for col in range(N):
            for dr, dc in pat:
                if judge(row, col, dr, dc):
                    return True
    return False


print("Yes" if solve() else "No")