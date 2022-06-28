import sys


remainders = []
for _ in range(10):
    num = int(sys.stdin.readline())
    remainders.append(num%42)

print(len(list(set(remainders))))
