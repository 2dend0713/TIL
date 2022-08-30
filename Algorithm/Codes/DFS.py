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


# DFS by recursive function

def DFS_recursive(node, visited=[]):
    visited.append(node)  # 방문 처리

    for next_node in G[node]:  # 인접 노드 탐색
        if next_node not in visited:
            visited = DFS_recursive(next_node, visited)  # 방문 처리된 리스트를 들고 재귀 수행
    return visited


print(f'result of DFS by recursive function: {DFS_recursive(1)}')


# DFS by stack

def DFS_stack(node):
    visited = []
    stack = [node]

    while stack:
        node = stack.pop()  # 현재 노드
        if node not in visited:
            visited.append(node)  # 방문 처리
            for next_node in G[node]:  # 인접 노드 탐색
                stack.append(next_node)
    return visited


print(f'result of DFS using stack: {DFS_stack(1)}')
