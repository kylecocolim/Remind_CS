# https://www.acmicpc.net/problem/5214
from collections import defaultdict
def sol(m,n,map_):
    graph = defaultdict(list)
    for sub in map_:
        graph[int(sub[0])].extend([int(sub[1]),int(sub[2])])

    def dfs(graph,start):
        stack = list()
        visit = list()
        mindist = int()
        stack.append(start)
        while stack:
            node = stack.pop()
            if node == target:
                mindist = min(mindist,len(visit))
            if node not in visit:
                visit.append(node)
                stack.extend(graph[node])
m ,n ,k = map(int,input().split())
map_ = [ input().split() for i in range(k)]
sol(m,n,map_)