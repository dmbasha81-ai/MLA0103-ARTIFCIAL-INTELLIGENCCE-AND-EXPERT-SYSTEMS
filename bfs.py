from collections import deque

# Graph represented using adjacency list
graph = {
    1: [2, 3],
    2: [1, 5, 6],
    3: [1, 4, 7],
    4: [3, 8],
    5: [2],
    6: [2],
    7: [3, 8],
    8: [4, 7]
}

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)

    while queue:
        node = queue.popleft()
        print(node, end=" ")

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

# Driver code
print("BFS Traversal:")
bfs(graph, 1)
