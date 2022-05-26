import sys


T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    R, S = sys.stdin.readline().split()

    result = ''
    for char in S:
        result += char * int(R)

    print(result)
