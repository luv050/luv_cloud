

n = int(input("Enter number of nodes: "))
p= input("Goal Node:")

graph = {}


print("Enter edges in the format 'node1 node2'.")
for i in range(n):
    node, *neighbors = input("Enter node and its roots separated by spaces: ").split()
    graph[node] = neighbors


visited = [] 
queue = []     

def bfs(visited, graph, node): 
    visited.append(node)
    queue.append(node)

    while queue:          
        m = queue.pop(0) 
        print(m, end=" ") 
        if m==p:
            print("\n" + p + " is the goal node and is found!")
            print("Path:", ' -> '.join(visited))
            break

        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)


print("\nFollowing is the Breadth-First Search:")
bfs(visited, graph, 'a')
