

n = int(input("Enter number of nodes: "))
root = input("Enter the root node: ")
goal_node = input("Enter the goal node: ")

graph = {}

print("Enter edges in the format 'node root1 root2 ...'.")
for _ in range(n):
    node, *neighbors = input("Enter node and its roots separated by spaces: ").split()
    graph[node] = neighbors

visited = []

def dfs(visited, graph, node, goal_node):
    if node not in visited:
        print(node)
        visited.append(node)
        if node == goal_node:
            print( node, " is a goal node and is found")
            return True
        for neighbour in graph[node]:
            if dfs(visited, graph, neighbour, goal_node):
                return True
    return False

# Driver Code
print("Depth-First Search (DFS):")
dfs(visited, graph, root, goal_node)
