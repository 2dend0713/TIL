import sys


N = int(sys.stdin.readline().rstrip())

num, cnt = 1, 0
while True:
    if '666' in str(num):
        cnt += 1

    if cnt == N:
        print(num)
        break

    num += 1
