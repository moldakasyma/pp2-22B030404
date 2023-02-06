import math


def is_prime(n):
    for i in range(2, int(math.sqrt(n))):
        if n % i == 0:
            return False
    return True


def return_primes(arr):
    return list(filter(lambda x : is_prime(x), arr))


l=list(map(int,input().split()))
print(return_primes(l))