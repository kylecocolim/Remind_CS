from BasicUtil import CreateRandArr , Swap


def BubbleSort(arr):
    for i in range(len(arr)-1):
        for j in range(i,len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = Swap(arr[i],arr[j])            
                # arr[i] , arr[j] = arr[j] , arr[i]
    return arr

if __name__ == "__main__":
    arr = CreateRandArr()
    print(arr)
    print(BubbleSort(arr))
