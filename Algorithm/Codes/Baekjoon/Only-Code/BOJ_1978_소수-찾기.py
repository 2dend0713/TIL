import sys


def isPrime(num):
    result = True
    for n in range(2, int(num**(1/2))+1):
        if num % n == 0:
            result = False
            break
    return result


N = int(sys.stdin.readline())
NUMS = list(map(int, sys.stdin.readline().split()))

ans = 0
for num in NUMS:
    if num != 1 and isPrime(num):
       ans += 1

print(ans)
