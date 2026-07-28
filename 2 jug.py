from collections import deque

capacity = (12, 8, 5)
start = (12, 0, 0)
goal = (6, 6, 0)

queue = deque([(start, [start])])
visited = set()

while queue:
    state, path = queue.popleft()

    if state == goal:
        print("Solution Found:")
        for s in path:
            print(s)
        break

    if state in visited:
        continue

    visited.add(state)

    for i in range(3):
        for j in range(3):
            if i != j:
                temp = list(state)
                amount = min(temp[i], capacity[j] - temp[j])
                temp[i] -= amount
                temp[j] += amount
                new_state = tuple(temp)

                if new_state not in visited:
                    queue.append((new_state, path + [new_state]))
else:
    print("No Solution Exists")
