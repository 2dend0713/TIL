from collections import defaultdict
import heapq


# sample data

G = {
    1: [],
    2: [(1, 2)],
    3: [(1, 5), (2, 2), (4, 1)],
    4: [(5, 1)],
    5: [(6, 1)],
    6: [(7, 1)],
    7: [(8, 1)],
    8: [(1, 1)]
}


# Dijkstra using heapq

def dijkstra(graph, node_s):
    q = [(0, node_s)]  # 간선 정보를 저장하는 리스트
    distances = defaultdict(int)  # 최단 거리를 저장하는 딕셔너리

    while q:
        weight, node = heapq.heappop(q)  # 최소 가중치의 간선 정보

        if node not in distances:  # 아직 등록되어 있지 않다면
            distances[node] = weight  # 등록
            for node_n, weight_n in G[node]:
                weight_n += weight  # 가중치 갱신
                heapq.heappush(q, (weight_n, node_n))  # BFS로 간선 정보 저장
    return distances


distances = dijkstra(G, 3)
for node, distance in distances.items():
    print(f'shortest distance from 3 to {node} by Dijkstra: {distance}')
