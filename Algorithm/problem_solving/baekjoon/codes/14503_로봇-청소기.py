import sys
from collections import deque


def clean():
    cnt = 1
    field[r][c] = 2

    q = deque([(r, c, d)])
    while q:
        row, col, dire = q.popleft()

        for rot in range(4):
            dire = (dire + 3) % 4
            nrow, ncol = row + dy[dire], col + dx[dire]

            if not field[nrow][ncol]:
                cnt += 1
                field[nrow][ncol] = 2
                q.append((nrow, ncol, dire))
                break

            if rot == 3:
                dire_back = (dire + 2) % 4
                row_back, col_back = row + dy[dire_back], col + dx[dire_back]

                if field[row_back][col_back] == 1:
                    return cnt
                else:
                    q.append((row_back, col_back, dire))


n, m = map(int, sys.stdin.readline().split())
r, c, d = map(int, sys.stdin.readline().split())
field = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

print(clean())
