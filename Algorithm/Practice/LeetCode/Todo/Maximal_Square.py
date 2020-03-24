class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        # Making Filter And Sliding Window
        print(matrix)
                
                
matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Solution().maximalSquare(matrix)
window_size = 2
for i in range(len(matrix[0])-window_size):
    for j in range(window_size):
        print((i,j),matrix[i+j][i])
        
    print('\n')
