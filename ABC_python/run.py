cnt_nodes = []

for _ in range(394):
    a, b, c = map(int, input().split())
    cnt_nodes.append(a)
    cnt_nodes.append(b)
a = set(cnt_nodes)
print(len(a))