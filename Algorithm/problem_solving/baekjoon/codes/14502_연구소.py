import sys
from collections import deque
from itertools import combinations


def spread():
    visited = [[0] * m for _ in range(n)]
    for r, c in virus_loca:
        visited[r][c] = 2

    q = deque(virus_loca)
    while q:
        row, col = q.popleft()

        for d in range(4):
            nrow, ncol = row + dy[d], col + dx[d]
            if 0 <= nrow < n and 0 <= ncol < m and not visited[nrow][ncol] and field[nrow][ncol] != 1:
                visited[nrow][ncol] = 2
                q.append((nrow, ncol))
    return visited


n, m = map(int, sys.stdin.readline().split())
field = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

zero_loca = []
virus_loca = []
wall_cnt = 3
for r in range(n):
    for c in range(m):
        if field[r][c] == 2:
            virus_loca.append((r, c))
        elif field[r][c] == 0:
            zero_loca.append((r, c))
        elif field[r][c] == 1:
            wall_cnt += 1

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

safe_cnt = 0
for comb in combinations(zero_loca, 3):
    for r, c in comb:
        field[r][c] = 1

    # print((n * m) - (sum(map(sum, spread())) / 2) - wall_cnt)
    safe_cnt = max(n * m - (sum(map(sum, spread())) // 2) - wall_cnt, safe_cnt)

    for r, c in comb:
        field[r][c] = 0

print(safe_cnt)
