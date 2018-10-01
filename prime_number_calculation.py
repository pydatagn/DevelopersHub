def sieve_of_eratosthenes(n):
    prime_arr = [True for i in range(n + 1)]
    i = 2
    while (i * i <= n):
        if (prime_arr[i] == True):
            for j in range(i * 2, n + 1, i):
                prime_arr[j] = False
        i += 1
    for i in range(2, n):
        if prime_arr[i]:
            print(i)


if __name__ == '__main__':
    n = 30
    print ("All prime numbers before ", n)
    sieve_of_eratosthenes(100)

