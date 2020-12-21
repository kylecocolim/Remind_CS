def shortestPathBFS(graph, start, end):
    visited = set([start])
    prev = {}
    queue = [start]
    while len(queue)>0:
        node = queue.pop(0)
        if node == end: 
            break
        for neighbor in graph.neighbors(node):
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)
                prev[neighbor] = node 
    
    def path(node):
        shortest_path = [node]
        while node != start:
            node = prev[node]
            shortest_path.insert(0, node)
        return shortest_path, len(shortest_path)-1
    
    return path(node)


g = ([0, 5, 7, 8, 9], 4)
shortestPathBFS(g, 0, 9)
