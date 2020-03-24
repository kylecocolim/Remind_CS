class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        num = str(x)
        length = len(num)
        #Even
        if length % 2 == 0:
            idx = length/2
        else:
            idx = (length-1)/2
        
        for i in range(int(idx)):
            if(num[i] != num[length-1-i]):
                return False

        return True