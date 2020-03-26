from collections import defaultdict
arr = [1,2,3,4,5]

bucket = defaultdict(list)
for i in range(len(arr)-1):
    if i != 0:
        bucket[arr[i]].extend([arr[i-1]])

    bucket[arr[i]].extend([arr[i+1]])

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

print(dfs(bucket,2))