import sys
from collections import deque


def investigate(row, col):
    visited[row][col] = 1
    q = deque([(row, col)])

    while q:
        r, c = q.popleft()
        for d in range(4):
            nr, nc = r + dy[d], c + dx[d]
            if FIELD[nr][nc] and not visited[nr][nc]:
                visited[nr][nc] = 1
                q.append((nr, nc))
            elif not FIELD[nr][nc]:
                melted_heights[r][c] += 1


N, M = map(int, sys.stdin.readline().split())
FIELD = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

result = 0
while True:
    visited = [[0] * M for _ in range(N)]
    melted_heights = [[0] * M for _ in range(N)]
    flag = 0
    for r in range(N):
        for c in range(M):
            if FIELD[r][c] and not visited[r][c]:
                flag += 1
                investigate(r, c)

    for r in range(N):
        for c in range(M):
            FIELD[r][c] -= melted_heights[r][c]
            if FIELD[r][c] < 0:
                FIELD[r][c] = 0
    result += 1

    if flag >= 2:
        print(result-1)
        break
    elif flag == 0:
        print(0)
        break
