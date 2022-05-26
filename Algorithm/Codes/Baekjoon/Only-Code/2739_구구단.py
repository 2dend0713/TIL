import sys


N = int(sys.stdin.readline().rstrip())

for step in range(1, 10):
    print(f'{N} * {step} = {N*step}')
