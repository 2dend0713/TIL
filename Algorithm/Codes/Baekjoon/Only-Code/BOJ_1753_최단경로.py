import sys
import heapq


def find_shortest(node_s):
    q = []
    heapq.heappush(q, (0, node_s))  # 다익스트라 알고리즘을 따르기 위해 가중치 우선 저장
    distances[node_s] = 0

    while q:
        weight, node = heapq.heappop(q)

        for weight_n, node_n in G[node]:
            distance_n = weight_n + weight  # 다음 노드로 가는 새로 계산한 거리
            if distance_n < distances[node_n]:  # 새로 계산한 거리가 더 짧다면
                distances[node_n] = distance_n  # 거리 갱신
                heapq.heappush(q, (distance_n, node_n))


V, E = map(int, sys.stdin.readline().split())
K = int(sys.stdin.readline())
G = [[] for _ in range(V+1)]
for _ in range(E):
    node_s, node_e, weight = map(int, sys.stdin.readline().split())
    G[node_s].append((weight, node_e))  # INPUT
distances = [9999999] * (V+1)  # 최단 거리 저장을 위한 리스트 초기화

find_shortest(K)  # K 노드부터 나머지 노드들까지 최단 거리 계산 by 다익스트라

for i in range(1, V+1):
    print('INF') if distances[i] == 9999999 else print(distances[i])  # OUTPUT
