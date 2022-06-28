import sys


while True:
    A, B = map(int, sys.stdin.readline().split())
    if not A and not B:
        break

    print(A+B)
