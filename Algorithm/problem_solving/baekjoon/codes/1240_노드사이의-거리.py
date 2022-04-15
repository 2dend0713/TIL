import sys
from collections import deque


def get_dist(start, end):
    visited = [0] * (n + 1)
    visited[start] = 1

    q = deque([(start, 0)])
    while q:
        s, distance = q.popleft()

        if s == end:
            return distance

        for nxt, dist in graph[s]:
            if not visited[nxt]:
                visited[nxt] = 1
                q.append((nxt, distance+dist))


n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    s, e, dist = map(int, sys.stdin.readline().split())
    graph[s].append((e, dist))
    graph[e].append((s, dist))

for _ in range(m):
    s, e = map(int, sys.stdin.readline().split())
    print(get_dist(s, e))
