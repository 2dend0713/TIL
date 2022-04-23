import sys


def find_gears_to_rotate(idx, dire):
    targets = [0] * 4  # dire 저장
    targets[idx] = dire

    for i in range(idx-1, -1, -1):  # 왼쪽 확인
        if gears[i][2] == gears[i+1][6]:
            break
        targets[i] = targets[i+1] * -1
    for i in range(idx+1, 4):  # 오른쪽 확인
        if gears[i][6] == gears[i-1][2]:
            break
        targets[i] = targets[i-1] * -1
    return targets


def rotate(idx, dire):
    if dire == 1:
        gears[idx] = [gears[idx][7]] + gears[idx][0:7]
    elif dire == -1:
        gears[idx] = gears[idx][1:] + [gears[idx][0]]


gears = [list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(4)]
k = int(sys.stdin.readline())

for _ in range(k):
    gear_i, d = map(int, sys.stdin.readline().split())
    targets = find_gears_to_rotate(gear_i-1, d)

    for idx, dire in enumerate(targets):
        if dire:
            rotate(idx, dire)

ans = 0
for idx, gear in enumerate(gears):
    if gear[0]:
        ans += gear[0] * (2 ** idx)
print(ans)
