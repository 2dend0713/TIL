import sys


N = int(sys.stdin.readline().rstrip())
A = set(sys.stdin.readline().split())
M = int(sys.stdin.readline().rstrip())
NUMS = sys.stdin.readline().split()

for num in NUMS:
    if num in A:
        print('1')
    else:
        print('0')
