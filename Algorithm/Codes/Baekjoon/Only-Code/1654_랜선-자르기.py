import sys


K, N = map(int, sys.stdin.readline().split())
LANS = [int(sys.stdin.readline().rstrip()) for _ in range(K)]

left, right = 1, max(LANS)

while left <= right:
    mid = (left + right) // 2
    cnt = sum(lan // mid for lan in LANS)

    if cnt >= N:
        left = mid + 1
    else:
        right = mid - 1

print(right)
