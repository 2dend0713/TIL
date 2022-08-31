import sys


N = int(sys.stdin.readline())

for num in range(1, N+1):
    # print(f'{num} : {list(str(num))}')
    if num + sum(map(int, list(str(num)))) == N:
        print(num)
        break
else:
    print(0)
