# https://leetcode.com/problems/k-concatenation-maximum-sum/
# Time exceed
class Solution:
    def kConcatenationMaxSum(self,arr,k):
        origin_arr = list(arr)
        maxNum = 0
        min_prefix_sum = 0
        # Repeat K
        for i in range(k-1):
            arr.extend(origin_arr)
        print(arr)
        prefixArr = []
        prefixArr.append(arr[0])
        for i in range(1,len(arr)):
            prefixArr.append(prefixArr[i-1]+arr[i])

        
        for i in range(len(arr)):
            maxNum = max(maxNum,prefixArr[i]-min_prefix_sum)
            min_prefix_sum = min(min_prefix_sum,prefixArr[i])
        return maxNum
arr = [1,2]
k= 3
        
print(Solution().kConcatenationMaxSum(arr,k))