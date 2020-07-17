# https://app.codility.com/programmers/lessons/4-counting_elements/perm_check/


def PermCheck(A):
    # Each Element is Only Once in Array
    elementDict = dict()
    for element in A:
        elementDict[element] = 1
    keys = elementDict.keys()
    for i in range(len(A)):
        if(i+1 not in keys):
            return 0

    return 1

A = [4,1,2,3]
PermCheck(A)

