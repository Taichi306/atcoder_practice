import numpy as np

a, b, c = map(int, input().split())

ans = np.roots([a, 0, 0, 0, b, c])
ans = str(ans[-1])
print(ans[1:-4])