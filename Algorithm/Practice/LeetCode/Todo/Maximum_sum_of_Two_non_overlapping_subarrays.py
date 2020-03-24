class Solution:
    def maxSumTwoNoOverlap(self, A, L: int, M: int) -> int:
    
        L_max = sum(A[0:L])
        L_idx = 0              
        for i in range(1,len(A)-L+1):
            if L_max < sum(A[i:i+L]):
                L_max = sum(A[i:i+L])
                L_idx = i
        print(L_idx)
        for j in range(L):
            A.pop(L_idx+j)             
        m_max = sum(A[0:M])
        for i in range(1,len(A)-M+1):
            m_max = max(sum(A[i:i+M]),m_max)
        return L_max + m_max
A = [3,8,1,3,2,1,8,9,0]
L = 3
M = 2
print(Solution().maxSumTwoNoOverlap(A,L,M))
