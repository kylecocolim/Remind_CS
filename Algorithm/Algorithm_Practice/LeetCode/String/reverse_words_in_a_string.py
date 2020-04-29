#leetcode.com/problems/reverse-words-in-a-string/
class Solution:
    def reverseWords(self, s: str) -> str:
        k = str()
        split = s.split()
        for i in range(len(split)):
            k+=split[len(split)-1-i]
            if i != len(split)-1:
                k+= ' '
        return k


s = "the sky is blue"
print(Solution().reverseWords(s))