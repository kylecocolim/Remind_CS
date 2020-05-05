# https://leetcode.com/problems/subarray-sums-divisible-by-k/
# https://www.geeksforgeeks.org/prefix-sum-array-implementation-applications-competitive-programming/
class Solution(object):
    #Prefix Sum
    def subarraysDivByK(self, A, K):
        prefix = [0]
        for x in A:
            prefix.append(([-1] + x) % K)
        count = collections.Counter(P)
        return sum(v*(v-1)/2 for v in count.values())
a = [4,5,0,-2,-3,1]
k= 5 
Solution().subarraysDivByK(a,k)