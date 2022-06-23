import sys


N = int(sys.stdin.readline())
NUMS = list(map(int, sys.stdin.readline().split()))

print(min(NUMS), max(NUMS))
