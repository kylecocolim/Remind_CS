class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        # 1+1 = 10
        # Different Length
        result = str()
        carry = 0
        A = list(a)
        B = list(b)
        
        while A or B or carry:
            if A:
                carry += int(A.pop())
            if B:
                carry += int(B.pop())
            result = str(carry%2) + result
            carry //=2
        return result
a = "11"
b = "1"
print(Solution().addBinary(a,b))