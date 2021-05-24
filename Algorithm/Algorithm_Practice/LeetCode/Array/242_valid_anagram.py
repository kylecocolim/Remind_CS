
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        _dict = dict()
        if(len(s) != len(t)):
            return False
        for _s,_t in zip(s,t):
            if(_s in _dict):
                _dict[_s] +=1
            else:
                _dict[_s] = 1
            if(_t in _dict):
                _dict[_t] -=1
            else:
                _dict[_t] = -1
        for _ ,value in _dict.items():
            if(value != 0):
                return False 
        return True
s = 'rat'
t = 'car'
sol = Solution().isAnagram(s,t)
print(sol)