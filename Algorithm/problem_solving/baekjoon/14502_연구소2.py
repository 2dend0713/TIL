import sys
import copy
from collections import deque


def spread():
    global safe_cnt

    q = deque()
    field_copied = copy.deepcopy(field)
    for r in range(n):
        for c in range(m):
            if field_copied[r][c] == 2:
                q.append((r, c))

    while q:
        row, col = q.popleft()

        for d in range(4):
            nrow, ncol = row + dy[d], col + dx[d]
            if 0 <= nrow < n and 0 <= ncol < m and field_copied[nrow][ncol] == 0:
                field_copied[nrow][ncol] = 2
                q.append((nrow, ncol))

    cnt = 0
    for r in range(n):
        for c in range(m):
            if field_copied[r][c] == 0:
                cnt += 1
    safe_cnt = max(safe_cnt, cnt)


def construct(step=0):
    if step == 3:
        spread()
        return

    for r in range(n):
        for c in range(m):
            if field[r][c] == 0:
                field[r][c] = 1
                construct(step+1)
                field[r][c] = 0


n, m = map(int, sys.stdin.readline().split())
field = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

safe_cnt = 0
construct()

print(safe_cnt)
