from collections import defaultdict
from itertools import combinations

class Solution():
    def letterCombinations(digits):
        alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        digitDict = defaultdict(list)
        ptr = 2
        for idx in range(len(alphabet)):
            
            digitDict[ptr].append([alphabet[idx]])

        print(digitDict)
digits = '23'

Solution.letterCombinations(digits)