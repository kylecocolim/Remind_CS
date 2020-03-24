
def bfs(graph,start):
    queue = list() 
    visited = list() 
    visited.append(start)
    while queue:
        node = queue.pop(0)
        if node not in visit:
            visit.append(node)
            queue.extend(graph[node])

    return visited
    