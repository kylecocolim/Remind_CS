#https://leetcode.com/problems/find-the-duplicate-number/
class Solution(object):
    def findDuplicate(self, nums):
        p = dict()
        for i in nums:
            if i not in p:
                p[i] = 1
            else:
                return i
