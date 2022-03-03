n = list(input())
d = len(n)
ans = 0

def pick(bit):
    use = []
    for i in range(d):
        if (bit >> i) % 2 == 1:
            use.append(n[i])
    use.sort(reverse=True)
    return int(''.join(use))

for bit in range(1, (1 << d)-1):
    other = ((1 << d) - 1) ^ bit
    ans = max(ans, pick(bit) * pick(other))

print(ans)