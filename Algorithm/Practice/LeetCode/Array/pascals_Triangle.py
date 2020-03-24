# 118. Pascal`s Triangle 
# leetcode.com/problems/pascals-triangle

class Solution(object):
    def generate(self, numRows):
        result = []
        for row in range(numRows):
            sub = []
            for col in range(0,row+1):
                if col == 0 or col == row:
                    sub.append(1)
                else:
                    sub.append(result[row-1][col-1]+result[row-1][col])
            result.append(sub)
        return result 

if __name__ == "__main__":
    
    testcase = [2,3,4,5,7]
    for numRows in testcase:
        problem = Solution().generate(numRows)
        print(problem)