# Problem : https://programmers.co.kr/learn/courses/30/lessons/12978
# Ref : https://mattlee.tistory.com/50


from heapq import *
from collections import defaultdict
def solution(N,road,K):
    graph = defaultdict(list)
    queue = [] 
    for src,dst,weight in road:
        graph[src].append([dst,weight])
        graph[dst].append([src,weight])    
    start = 1
    queue = []
    distance = {node : float('inf') for node in graph.keys() }
    distance[start] = 0
    heappush(queue,[0,start])
    while queue:
        curr_distance,curr_node = heappop(queue)
        for dst,weight in graph[curr_node]:
            if distance[dst] > curr_distance + weight:
                distance[dst] = curr_distance + weight 
                heappush(queue,[distance[dst],dst])
    cnt = 0
    for key, value in distance.items():
        if value <= K:
            cnt+=1

    return cnt

N = 5
road = [[1, 2, 1], [2, 3, 3], [5, 2, 2], [1, 4, 2], [5, 3, 1], [5, 4, 2]] 
K = 3
solution(N,road,K)