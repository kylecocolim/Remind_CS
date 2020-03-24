class Solution(object):
    def lengthOfLastWord(self,s):
        if len(s) > 0:
            token = s.split()
            if len(token) == 0:
                return len(token)
            else:
                return len(token[-1])
        else:
            return 0

s= ""
print(Solution().lengthOfLastWord(s))