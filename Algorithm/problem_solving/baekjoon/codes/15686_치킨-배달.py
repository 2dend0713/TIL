import sys
from itertools import combinations


def get_dist(row, col, stores):
    dist = 2 * n
    for store in stores:
        dist = min(abs(store[0]-row) + abs(store[1]-col), dist)
    return dist


def select_stores():
    global ans

    for comb in combinations(stores, m):  # 가게(r, c) 선택
        sum = 0
        for home in homes:
            sum += get_dist(home[0], home[1], comb)
        ans = min(sum, ans)


n, m = map(int, sys.stdin.readline().split())
field = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

homes = []
stores = []
for r in range(n):
    for c in range(n):
        if field[r][c] == 1:
            homes.append((r, c))
        elif field[r][c] == 2:
            stores.append((r, c))

ans = n ** 2 * (2 * n)
select_stores()

print(ans)
