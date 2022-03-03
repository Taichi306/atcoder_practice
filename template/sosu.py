from operator import is_


def isPrime(n):
    if n == 1:
        return True
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# --------------------------------------------
print(isPrime(2))
print(int(2**0.5)+1-1)

for i in range(10, 1):
    print(i)