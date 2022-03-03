def eratosthenes(n):
    prime_list = []
    num_list = [i for i in range(2, n+1)]
    
    while True:
        if int(n**0.5) <= num_list[0]:
            return prime_list + num_list
        prime_list.append(num_list[0])
        num_list = [e for e in num_list if e % num_list[0] != 0]

max_lr = 100
er_list = eratosthenes(max_lr)
print(er_list)