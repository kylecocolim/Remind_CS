
def solution(A):
    if len(A) > 0:
        elementDict = dict()
        for element in A:
            if element in elementDict.keys():
                elementDict[element] += 1
            else:
                elementDict[element] = 1
        
        arr = sorted(elementDict.items() , key = lambda x : x[1], reverse=True)
        print(arr)
        for item in arr:
            if(item[0] == item[1]):
                return item[0]
        
        return 0
    else:
        return 0 
    

A = [1,5,5,5,5,5]
print(solution(A))