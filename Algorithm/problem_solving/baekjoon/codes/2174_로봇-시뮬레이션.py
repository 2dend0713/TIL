import sys
from collections import defaultdict


def perform_order(robot_idx, order, rep):
    robot_idx, rep = int(robot_idx), int(rep)

    if order == 'L':
        for _ in range(rep%4):
            robots[robot_idx][2] = (robots[robot_idx][2] + 3) % 4
    elif order == 'R':
        for _ in range(rep%4):
            robots[robot_idx][2] = (robots[robot_idx][2] + 1) % 4
    elif order == 'F':
        for _ in range(rep):
            nx, ny = robots[robot_idx][0] + dx[robots[robot_idx][2]], robots[robot_idx][1] + dy[robots[robot_idx][2]]

            if not (0 <= nx < a and 0 <= ny < b):
                return f'Robot {robot_idx} crashes into the wall'
            elif field[ny][nx]:
                return f'Robot {robot_idx} crashes into robot {field[ny][nx]}'
            else:
                field[robots[robot_idx][1]][robots[robot_idx][0]], field[ny][nx] = 0, robot_idx
                robots[robot_idx][0], robots[robot_idx][1] = nx, ny


a, b = map(int, sys.stdin.readline().split())
n, m = map(int, sys.stdin.readline().split())
direction = {'N': 0, 'E': 1, 'S': 2, 'W': 3}
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

field = [[0] * a for _ in range(b)]
robots = defaultdict(list)

for robot_idx in range(1, n+1):
    x_str, y_str, dire = sys.stdin.readline().split()
    x, y, d = int(x_str) - 1, (b - int(y_str)), direction[dire]

    field[y][x] = robot_idx
    robots[robot_idx] = [x, y, d]

for _ in range(m):
    ans = perform_order(*sys.stdin.readline().split())

    if ans:
        print(ans)
        break
else:
    print('OK')
