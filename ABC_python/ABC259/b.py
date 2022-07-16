import numpy as np
import math

a, b, d = map(int, input().split())

def sin(x):
    return math.sin(math.radians(x))

def cos(x):
    return math.cos(math.radians(x))

det1 = np.array([[cos(d), -sin(d)], [sin(d), cos(d)]])
det2 = np.array([a, b])
ans = np.dot(det1, det2)
print(*ans)