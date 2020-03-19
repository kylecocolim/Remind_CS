# https://www.acmicpc.net/problem/2606 

from collections import defaultdict
def Virus(arr,infected_node):
    def dfs(graph,start):
        visit = []
        stack = []
        stack.append(start)
        while stack:
            node = stack.pop()
            if node not in visit:
                visit.append(node)
                stack.extend(graph[node])
        return visit

    graph = defaultdict(list)
    for i in arr:
        graph[i[0]].extend([i[1]])

    return len(dfs(graph,infected_node)) - 1

graph = [[1,2],[2,3],[1,5],[5,2],[5,6],[4,7]]
print(Virus(graph,1))