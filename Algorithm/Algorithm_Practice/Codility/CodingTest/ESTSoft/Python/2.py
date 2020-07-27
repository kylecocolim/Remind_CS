from collections import defaultdict
from itertools import permutations
def solution(A):
    if len(A) > 0:
        digitSum = defaultdict(list)
        for number in A:
            tmpSum = 0
            for digit in str(number):
               tmpSum += int(digit)
            
            digitSum[tmpSum].append(number)
        result = -1
        for key,value in digitSum.items():
            if len(value) >=2:
                value = sorted(value , reverse=True)
                result = max(result,value[0]+value[1])
        return result
    else:
        return -1

A = [51,71,17,42]
print(solution(A))