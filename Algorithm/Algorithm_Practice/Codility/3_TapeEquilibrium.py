# https://app.codility.com/programmers/lessons/3-time_complexity/tape_equilibrium/
def TapeEquilibrium(A):
    if(len(A)> 1):
        prefixSumArray = [] 
        prefixSumArray.append(A[0])
        for idx in range(1,len(A)):
            prefixSumArray.append(prefixSumArray[idx-1]+A[idx])
        result = 100001
        for i in range(len(A)-1):
            result =min(result,abs(prefixSumArray[-1]-prefixSumArray[i]-A[i]))
            
        print(result)

    else:
        return A[0]

A = [3,1,2,4,3]
TapeEquilibrium(A)