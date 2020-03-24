class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        #s SubSequence
        #t Target 
        k = []
        idx = 0
        for target in t:
            l = []
            for i in range(idx,len(s)):
                if s[i] == target:
                    l.append(i)
            idx+=1
            k.append(l)
        for i in range(len(k)):
            for j in range(len(k[0])):
                

s= 'rabbitrabbit'
t = 'rabbit'

Solution().numDistinct(s,t)