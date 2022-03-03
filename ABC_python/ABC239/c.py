import numpy as np
 
x1, y1, x2, y2 = map(int, input().split())
 
iti = np.array([x1, y1])
ni = [x2, y2]
init = []
kakeru = [[1, 2], [2, 1], [-1, 2], [-2, 1], [1, -2], [2, -1], [-1, -2], [-2, -1]]
 
for i in range(8):
    init.append(iti+kakeru[i])
 
ans = []
for i in range(8):
    for j in range(8):
        ans.append(init[i]+kakeru[j])


for i in range(len(ans)):
    if all(ans[i] == ni):
        print('Yes')
        exit()
    else:
        pass
 
print('No')