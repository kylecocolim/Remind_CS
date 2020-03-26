# https://programmers.co.kr/learn/courses/30/lessons/43162
# Network 
from collections import defaultdict
def Network(n, computers):
    def dfs(graph,start):
        stack = list()
        visited = list() 
        stack.append(start)
        while stack:
            node = stack.pop()
            if node not in visited:
                visited.append(node)
                stack.extend(graph[node])
        return visited

    
    connection = defaultdict(list)
    for i in range(len(computers)):
        for j in range(n):
            if computers[i][j] == 1:
                connection[i].extend([j])
    
    nodes = [0 for i in range(n)]
    network_count = 0
    for i in range(n):
        if nodes[i] == 0:
            visited = dfs(connection,i)
            for k in visited:
                nodes[k] = 1

            network_count +=1 


    return network_count


if __name__ == "__main__":
    n = 3
    Nodes = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
    print(Network(n,Nodes))