class Solution(object):
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        table = dict()
        for source, target, cost in times:
            try:
                table[source].append((target,cost))
            except:
                table[source] = [(cost,target)]        
        dist = {node: float('inf') for node in range(1, N+1)}
        print(dist)
        def dfs(node, elapsed):
            if elapsed >= dist[node]: return
            dist[node] = elapsed
            for time, nei in sorted(table[node]):
                dfs(nei, elapsed + time)
        dfs(K, 0)
        print(dist)

if __name__ == "__main__":
    times = [[2,1,1],[2,3,1],[3,4,1]]
    # times : Source Node , Target Node , Time Fly
    N = 4
    K = 2
    Solution().networkDelayTime(times,N,K)