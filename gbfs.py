import heapq
# Graph
graph = {
    'A': ['B', 'C', 'D'],
    'B': ['E'],
    'C': ['E', 'F'],
    'D': ['F'],
    'E': ['H'],
    'F': ['G'],
    'H': ['G'],
    'G': []
}

# Heuristic values h(n)
heuristic = {
    'A': 40,
    'B': 32,
    'C': 25,
    'D': 35,
    'E': 19,
    'F': 17,
    'H': 10,
    'G': 0
}

def gbfs(start, goal):
    pq = []
    heapq.heappush(pq, (heuristic[start], start))
    visited = set()
    parent = {start: None}
    while pq:
        h, node = heapq.heappop(pq)
        if node in visited:
            continue
        visited.add(node)
        if node == goal:
            path = []
            while node:
                path.append(node)
                node = parent[node]
            path.reverse()
            print("Path:", " -> ".join(path))
            return
        for neighbor in graph[node]:
            if neighbor not in visited:
                parent[neighbor] = node
                heapq.heappush(pq, (heuristic[neighbor], neighbor))
    print("Goal not found")
# Driver Code
gbfs('A', 'G')



Algorithm GBFS(Start, Goal)

1. Create an empty Priority Queue OPEN.
2. Insert Start into OPEN with heuristic value h(Start).
3. Create an empty set VISITED.

4. While OPEN is not empty do
      a. Remove the node with the smallest heuristic value.
      b. If the node is Goal,
            Return Success.
      c. Mark the node as VISITED.
      d. For each neighbor of the current node
            If neighbor is not in VISITED
                 Insert neighbor into OPEN with h(neighbor).

5. Return Failure (Goal not found).

End Algorithm
