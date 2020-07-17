

def MissingInteger(A):
    # Must be greater than 0 
    if len(A) > 0:
        elementDict = dict()
        MaxInteger = -1000001
        missingInteger = int()
        for element in A:
            if element > 0:
                elementDict[element] = 1
                MaxInteger = max(MaxInteger,element)
        keys = elementDict.keys()


        for idx in range(MaxInteger):
            if idx+1 not in keys:
                missingInteger = idx+1
        if (missingInteger == 0 and MaxInteger > 0):
            return MaxInteger + 1
        elif(missingInteger == 0 and MaxInteger < 0):
            return 1
        else:
            return missingInteger
    else:
        return 1
A = [1, 3, 6, 4, 1, 2]
A = [-1,-2]
print(MissingInteger(A))