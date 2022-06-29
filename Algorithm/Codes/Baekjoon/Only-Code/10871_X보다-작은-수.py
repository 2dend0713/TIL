import sys


N, X = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))

for num in A:
    if num < X:
        print(num, end=' ')
