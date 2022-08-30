# sample data

G = {
    1: [2, 3, 4],
    2: [5],
    3: [5],
    4: [],
    5: [6, 7],
    6: [],
    7: [3]
}


# BFS by queue

def BFS(node):
    visited = [node]
    queue = [node]

    while queue:
        node = queue.pop(0)  # 현재 노드
        for next_node in G[node]:
            if next_node not in visited:
                visited.append(next_node)  # 방문 처리
                queue.append(next_node)
    return visited


print(f'result of BFS using queue: {BFS(1)}')


from collections import deque