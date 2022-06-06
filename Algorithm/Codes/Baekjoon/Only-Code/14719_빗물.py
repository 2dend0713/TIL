import sys


R, C = map(int, sys.stdin.readline().split())
AREA = list(map(int, sys.stdin.readline().split()))

max_height, result = max(AREA), 0
for height in range(max_height, 0, -1):
    flag, cnt = False, 0
    for c in range(C):
        if AREA[c] >= height:
            if flag:
                result, cnt = result + cnt, 0
            else:
                flag, cnt = True, 0
        else:
            cnt += 1

print(result)
