# https://app.codility.com/programmers/lessons/3-time_complexity/perm_missing_elem/

def PermMissElem(A):
    if len(A) > 0:
        N = len(A)
        result= ((N+1)*(N+2))/2
        for element in A:
            result -= element
        return int(result)
    else:
        return 0
        
A = [2,3,1,5]
print(PermMissElem(A))