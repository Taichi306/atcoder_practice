a, b, c = map(int, input().split())

_max = max(a*b, a*c, b*c)
_min = min(a*b, a*c, b*c)

print(_min, _max)