def CyclicRotation(A,K):
    if len(A) > 0:
        for iteration in range(K):
            last = A.pop(-1)
            tmpArr = []
            tmpArr.append(last)
            for element in A:
                tmpArr.append(element)
            A = tmpArr 
        return A
    else:
        return A
A = []
K = 3 

CyclicRotation(A,K)