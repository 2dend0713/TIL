import sys


def roll(dire):
    if dire == 1:
        dice[1], dice[4], dice[6], dice[3] = dice[4], dice[6], dice[3], dice[1]
    elif dire == 2:
        dice[1], dice[3], dice[6], dice[4] = dice[3], dice[6], dice[4], dice[1]
    elif dire == 3:
        dice[1], dice[5], dice[6], dice[2] = dice[5], dice[6], dice[2], dice[1]
    elif dire == 4:
        dice[1], dice[2], dice[6], dice[5] = dice[2], dice[6], dice[5], dice[1]


n, m, x, y, k = map(int, sys.stdin.readline().split())
field = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dice = [0] * 7
dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]

for dire in list(map(int, sys.stdin.readline().split())):
    nx, ny = x + dx[dire], y + dy[dire]
    if 0 <= nx < n and 0 <= ny < m:
        roll(dire)
        print(dice[1])

        x, y = nx, ny
        if field[x][y]:
            dice[6] = field[x][y]
            field[x][y] = 0
        else:
            field[x][y] = dice[6]
