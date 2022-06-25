import sys


H, M = map(int, sys.stdin.readline().split())

if 45 <= M <= 59:
    print(H, M-45)
elif 0 <= M < 45:
    if H == 0:
        print(23, M+15)
    else:
        print(H-1, M+15)
