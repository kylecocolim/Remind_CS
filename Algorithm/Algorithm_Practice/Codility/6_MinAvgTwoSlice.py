# 1. Sliding Windows
def solution(A):
    # Sliding Window 
    result = 10001
    for WindowSize in range(1,len(A)):
        for i in range(len(A)+1-WindowSize):
            result= min(result,int(sum(A[i:i+WindowSize])/WindowSize))
    return result
A = [4,2,2,5,1,5,8]
print(solution(A))