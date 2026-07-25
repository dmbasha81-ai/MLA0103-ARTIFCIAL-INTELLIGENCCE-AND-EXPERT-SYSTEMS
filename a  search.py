import heapq
# Graph: Node -> [(Neighbor, Cost)]
graph = {
    'S': [('A', 3), ('D', 4)],
    'A': [('S', 3), ('D', 5), ('B', 4)],
    'D': [('S', 4), ('A', 5), ('E', 2)],
    'B': [('A', 4), ('C', 4), ('E', 5)],
    'E': [('D', 2), ('B', 5), ('F', 4)],
    'C': [('B', 4)],
    'F': [('E', 4), ('G', 3.5)],
    'G': []
}

# Heuristic values h(n)
heuristic = {
    'S': 11.5,
    'A': 10,
    'D': 9,
    'B': 5,
    'E': 7,
    'C': 3,
    'F': 3,
    'G': 0
}

def astar(start, goal):
    open_list = []
    heapq.heappush(open_list, (heuristic[start], 0, start, [start]))
    visited = set()
    while open_list:
        f, g, node, path = heapq.heappop(open_list)
        if node == goal:
            print("Path:", " -> ".join(path))
            print("Total Cost:", g)
            return
        if node in visited:
            continue
        visited.add(node)
        for neighbor, cost in graph[node]:
            if neighbor not in visited:
                new_g = g + cost
                new_f = new_g + heuristic[neighbor]
                heapq.heappush(open_list,
                               (new_f, new_g, neighbor, path + [neighbor]))
    print("No Path Found")
# Driver Code
astar('S', 'G')


Algorithm A* Search(Start, Goal)

1. OPEN ← {Start}
2. CLOSED ← ∅
3. g(Start) ← 0
4. f(Start) ← g(Start) + h(Start)

5. While OPEN is not empty do
      a. Select node N from OPEN with the lowest f(N)
      b. Remove N from OPEN
      c. If N = Goal then
            Print the path
            Stop
      d. Add N to CLOSED

      e. For each neighbor M of N do
            If M is not in CLOSED then
                tentative_g ← g(N) + Cost(N, M)

                If M is not in OPEN OR tentative_g < g(M) then
                    Parent(M) ← N
                    g(M) ← tentative_g
                    f(M) ← g(M) + h(M)

                    If M is not in OPEN then
                        Add M to OPEN
                    End If
                End If
            End If
        End For
   End While

6. Print "Path Not Found"

End Algorithm
