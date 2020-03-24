#https://leetcode.com/problems/top-k-frequent-words/
import collections

class Solution(object):
    def topKFrequent(self,word, k):
        word = collections.Counter(word)
        sort = sorted(word.items(),key = lambda x: (-x[1],x[0].lower()))
        return [sort[i][0] for i in range(k)]
word = ["i", "love", "leetcode", "i", "love", "coding"]



print(Solution().topKFrequent(word,2))

