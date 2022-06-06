import sys


def isPrime(num):
    if num == 1:
        return False

    for divisor in range(2, int(num**(1/2))+1):
        if num % divisor == 0:
            return False

    return True


M, N = map(int, sys.stdin.readline().split())

for num in range(M, N+1):
    if isPrime(num):
        print(num)
