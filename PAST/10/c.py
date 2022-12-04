alpha = "abcdefghijklmnopqrstuvwxyz"

a = str(input())
cnt = 0

while len(a) > 3:
    a = a[:-3]
    cnt += 1
a = a + alpha[cnt-1]
print(a)