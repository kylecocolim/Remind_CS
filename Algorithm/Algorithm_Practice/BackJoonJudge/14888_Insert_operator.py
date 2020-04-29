# https://www.acmicpc.net/problem/14888
# Tag : Dynamic Programming 

def insertOperator(numArr,opArr):
    opstack = list()
    sequence = list()
    for idx in range(len(opArr)):
        if opArr[idx] != 0:
            for ctr in range(opArr[idx]):
                if idx % 4 == 0:
                    opstack.append('+')
                elif idx % 4 == 1:
                    opstack.append('-')
                elif idx%4 == 2:
                    opstack.append('*')
                elif idx%4 == 3:
                    opstack.append('/')
    if len(opstack) >= len(numArr):
        # False Opeartor
        # Must be little than Number
        return 0 
    def sequenceWorker(sequence):
        sum = numArr[0]
        for i in range(len(sequence)):
            if sequence[i] == '+':
                sum += numArr[i+1]
            elif sequence[i] == '-':
                sum -= numArr[i+1]
            elif sequence[i] == '*':
                sum *= numArr[i+1]
            elif sequence[i] == '/':
                sum = int(sum/numArr[i+1])
        return sum

    
    #  https://www.geeksforgeeks.org/heaps-algorithm-for-generating-permutations/  
    def heapPermutation(a, size, n): 
        if (size == 1): 
            num = sequenceWorker(a)
            return sequence.append(num)
        for i in range(size): 
            heapPermutation(a,size-1,n); 
            if size&1: 
                a[0], a[size-1] = a[size-1],a[0] 
            else: 
                a[i], a[size-1] = a[size-1],a[i] 
    heapPermutation(opstack,len(opstack),len(opstack))
    maxNum = max(sequence)
    minNum = min(sequence)
    print(maxNum,minNum)
  
n = input()
numArr = list(map(int,input().split()))
opArr = list(map(int,input().split()))
insertOperator(numArr,opArr)