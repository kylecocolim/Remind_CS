# https://leetcode.com/problems/maximum-subarray/
# Level : Easy 
# 2020-03-28

#Time Limit Exceed
class Solution(object):
    def maxSubArray(self,nums):
        if len(nums) == 1:
            return nums[0]
        if len(nums) > 0:
            calc = int()
            for WindowSize in range(1,len(nums)+1):
                for idx in range(0,len(nums)-WindowSize+1):
                    if(WindowSize == 1 and idx == 0):
                        calc = sum(nums[idx:idx+WindowSize])
                    else:
                        calc = max(calc,sum(nums[idx:idx+WindowSize])) 
            return calc 
        else:
            return 0

#From Discuss
class Solution2:
    def maxSubArray(self, nums):
        maxsum,currentsum = nums[0],nums[0]
        for i in nums[1:]:
            currentsum = max(i,currentsum+i)
            maxsum = max(maxsum,currentsum)
        return maxsum

arr =  [-2,-1]

sol = Solution() 
answer = sol.maxSubArray(arr)
print(answer)