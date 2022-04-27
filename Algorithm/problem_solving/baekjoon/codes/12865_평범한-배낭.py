import sys


def pack():
    for item_i in range(1, n+1):
        weight, value = items[item_i]
        for weight_bag in range(1, k+1):
            if weight_bag >= weight:
                cache[item_i][weight_bag] = max(cache[item_i-1][weight_bag-weight] + value, cache[item_i-1][weight_bag])
            else:
                cache[item_i][weight_bag] = cache[item_i-1][weight_bag]

    return cache[n][k]


n, k = map(int, sys.stdin.readline().split())
items = [(0, 0)] + [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]
cache = [[0] * (k + 1) for _ in range(n+1)]

print(pack())
