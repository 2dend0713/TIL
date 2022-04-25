import sys
from collections import deque


def check_validation(node):
    return 0 <= node < 100001


def find_target(start, target):
    visited = [False] * 100001
    visited[start] = True
    q = deque([(start, 0)])

    while q:
        start, time = q.popleft()
        if start == target:
            return time

        left, right, jump = start - 1, start + 1, start * 2
        if check_validation(jump) and not visited[jump]:
            visited[jump] = True
            q.appendleft((jump, time))
        if check_validation(left) and not visited[left]:
            visited[left] = True
            q.append((left, time+1))
        if check_validation(right) and not visited[right]:
            visited[right] = True
            q.append((right, time+1))


n, k = map(int, sys.stdin.readline().split())
print(find_target(n, k))
