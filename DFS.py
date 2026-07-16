graph={
    1: [2,3],
    2: [4,5],
    3:[],
    4:[5],
    5:[]
    }
visited=[]
def dfs(node):
    if node not in visited:
        print(node,end="")
        visited.append(node)
        for neighbour in graph(node):
            dfs(neighbour)
print("DFS Traversal:")
dfs(1)
