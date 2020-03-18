from BasicUtil import CreateRandArr , Swap, TestArr

def RadixSort(arr):
    sorted_bucket = [ list() for i in range(0,10)]
    index = 10
    iterator_count = 0
    count = 0
    while(True):
        bucket = [ list() for i in range(0,10)]
        if iterator_count == 0:   
            for number in arr:
                bucket[(number%10)].extend([number])
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

if __name__ == "__main__":
    RandArr = CreateRandArr(MaxNum=10000000000,ArrSize=1000)
    print(RadixSort(RandArr))
    #print(sorted(RandArr))