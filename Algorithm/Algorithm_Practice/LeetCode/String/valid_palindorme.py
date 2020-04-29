import datetime 
class Solution(object):
    def isPalindrome(self, s):
        # 0 ~ 9 : 
        # A ~ Z : 65 ~ 90 
        # a ~ z : 97 ~ 122
        k = str()
        for i in s.lower():
            if (ord(i) >=97 and ord(i) <=122) or (ord(i) >=48 and ord(i)<=57):
                k+=i
        for j in range(int(len(k)/2)):
            if (k[j] is not k[len(k)-1-j]):
                return False

        return True
past = datetime.datetime.now()
        

s = "A man, a plan, a canal: Panama"
s1 = "race a! car"
s2 = 'a'
print(Solution().isPalindrome(s2))
print(datetime.datetime.now()-past)