
def solution(A):
    # Find Triplet Value
    # Sort by Abs and escape odd Negative
    def RadixSort(arr):
        sorted_bucket = [ list() for i in range(0,10)]
        index = 10
        iterator_count = 0
        count = 0
        while(True):
            bucket = [ list() for i in range(0,10)]
            if iterator_count == 0:   
                for number in arr:
                    bucket[(abs(number)%10)].extend([number])
                    iterator_count +=1
            else:
                for numbers in sorted_bucket: 
                    for idx in range(len(numbers)):
                        arrIdx = int(numbers[idx]/index)%10
                        if(arrIdx == 0):
                            count += 1
                        bucket[arrIdx].extend([numbers[idx]])
                index *= 10
            sorted_bucket = bucket
            if count == len(arr):
                break 

            count =0
            
        return sorted_bucket[0]

    sortedArr = RadixSort(A)
    negPtr = []
    productArr = []
    idx = len(sortedArr)-1
    while True:
        
        print(sortedArr[idx])
        if(idx == 0):
            break

        idx -=1
        
        

A = [-3,1,2,-2,5,6]
solution(A)
        