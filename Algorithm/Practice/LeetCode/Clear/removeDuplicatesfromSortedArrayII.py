class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) != 0:
            stack = list()
            stack.append(nums[0])
            flag = 1
            stack_top = 0
            for i in range(1,len(nums)):
                if stack[stack_top] != nums[i]:
                    stack.append(nums[i])
                    stack_top+=1
                    flag = 0
                elif flag < 2 and stack[stack_top] == nums[i]:
                    stack.append(nums[i])
                    stack_top+=1
                    flag +=1
                flag+=1
            nums = stack
        return len(nums)        
                

nums = [0,0,0,1,1,1,1,1,1,1,2,2,2,2,2,2,2,3,3,3,3]
Solution().removeDuplicates(nums)