import sys
from pprint import pprint


def check_dire(dire):
    if dire == 'N':
        return 0
    elif dire == 'E':
        return 1
    elif dire == 'S':
        return 2
    elif dire == 'W':
        return 3


def perform_order(idx, order, rep):
    print(idx, order, rep)
    idx, rep = int(idx), int(rep)
    r, c, dire = robots[idx]
    print(r, c, dire)

    if order == 'L':
        for _ in range(rep):
            dire = (dire + 3) % 4
    elif order == 'R':
        for _ in range(rep):
            dire  = (dire + 1) % 4
    elif order == 'F':
        for _ in range(rep):
            if dire == 0:
                nr, nc = r - 1, c
            elif dire == 1:
                nr, nc = r, c + 1
            elif dire == 2:
                nr, nc = r + 1, c
            elif dire == 3:
                nr, nc = r, c - 1

            pprint(field)
            if not (0 <= nr <= b and 0 <= nc <= a):
                return f'Robot {idx} crashes into the wall'
            elif field[nr][nc]:
                return f'Robot {idx} crashes into robot {field[nr][nc]}'
            field[nr][nc] = field[r][c]
            field[r][c] = 0


a, b = map(int, sys.stdin.readline().split())
n, m = map(int, sys.stdin.readline().split())

field = [[0] * (a + 1) for _ in range(b+1)]
robots = [0]

for robot in range(n):
    x, y, dire = sys.stdin.readline().split()
    c, r, dire = int(x), b + 1 - int(y), check_dire(dire)
    field[r][c] = robot + 1
    robots.append((r, c, dire))

for _ in range(m):
    ans = perform_order(*sys.stdin.readline().split())
    print(ans)

    if ans:
        print(ans)
        break
else:
    print('OK')
