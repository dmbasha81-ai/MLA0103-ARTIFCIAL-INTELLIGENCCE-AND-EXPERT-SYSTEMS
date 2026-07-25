import heapq
# Graph with edge costs
graph = {
    'S': [('A', 1), ('G', 12)],
    'A': [('B', 3), ('C', 1)],
    'B': [('D', 3)],
    'C': [('D', 1), ('G', 2)],
    'D': [('G', 3)],
    'G': []
}

def ucs(graph, start, goal):
    priority_queue = [(0, start)]
    visited = set()

    while priority_queue:
        cost, node = heapq.heappop(priority_queue)

        if node in visited:
            continue

        visited.add(node)

        if node == goal:
            print("Goal found:", node)
            print("Minimum Cost:", cost)
            return

        for neighbor, weight in graph[node]:
            if neighbor not in visited:
                heapq.heappush(priority_queue, (cost + weight, neighbor))

ucs(graph, 'S', 'G')



Algorithm UCS(Graph, Start, Goal)

1. Create a priority queue PQ.
2. Insert (Start, Cost = 0) into PQ.
3. Mark all nodes as unvisited.

4. While PQ is not empty do
      a. Remove the node with the smallest cost from PQ.
      b. If the node is already visited,
            Continue.
      c. Mark the node as visited.
      d. If the node is the Goal,
            Print the total cost.
            Stop.
      e. For each neighboring node of the current node do
            If the neighbor is not visited then
                NewCost = CurrentCost + EdgeCost
                Insert (Neighbor, NewCost) into PQ.

5. If Goal is not found,
      Print "Goal not reachable".
