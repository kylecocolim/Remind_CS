#https://programmers.co.kr/learn/courses/30/lessons/43165?language=python3

#Counted by Class Member Variable
class Sol():
    def __init__(self):
        self.count =0
    def targetNumber(numbers,target):
        def recursion(idx,result,resultarr):
            if(len(numbers)==idx):
                if result == target:
                    self.count+=1
            else:
                recursion(idx+1,result+numbers[idx],resultarr)
                recursion(idx+1,result-numbers[idx],resultarr)
        if len(numbers) == 1:
            if target == numbers[0]:
                return 1
            else:
                return 0
        
        recursion(1,numbers[0],resultarr)
        recursion(1,-numbers[0],resultarr)
        return self.count

#Counted by list length
def targetNumber(numbers,target):
    def recursion(idx,result,resultarr):
        if(len(numbers)==idx):
            if result == target:
                resultarr.append(result)
        else:
            recursion(idx+1,result+numbers[idx],resultarr)
            recursion(idx+1,result-numbers[idx],resultarr)
    if len(numbers) == 1:
        if target == numbers[0]:
            return 1
        else:
            return 0
    
    resultarr = []
    recursion(1,numbers[0],resultarr)
    recursion(1,-numbers[0],resultarr)
    return len(resultarr)

numbers = [1,1]
target = 2
print(targetNumber(numbers,target))