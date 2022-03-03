a, b, c, d = map(int, input().split())
temp = b - a + 1
temp2 = d - c + 1

def isPrime(n):
    if n == 1:
        return True
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

takahashi = []
for i in range(a, b+1):
    takahashi.append(i)
aoki = [[] for _ in range(temp)]
for i in range(temp):
    for j in range(c, d+1):
        aoki[i].append(takahashi[i]+j)

ans = 0
for i in range(temp):
    temp_list = []
    for j in range(temp2):
        if isPrime(aoki[i][j]):
            temp_list.append(True)
    if temp_list:
        ans += 1
        
if ans == temp:
    print('Aoki')
else:
    print('Takahashi')