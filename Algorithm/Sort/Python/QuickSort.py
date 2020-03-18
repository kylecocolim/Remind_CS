# Explanation 
# https://gmlwjd9405.github.io/2018/05/10/algorithm-quick-sort.html
# https://ko.wikipedia.org/wiki/%ED%80%B5_%EC%A0%95%EB%A0%AC
from BasicUtil import CreateRandArr, Swap
def QuickSort(arr):  
    if len(arr) > 1:
        pivot = arr[len(arr)-1]
        left,mid,right = [] , [] , []
        for i in range(len(arr)-1):
            if arr[i] < pivot:
                left.append(arr[i])
            elif arr[i] > pivot:
                right.append(arr[i])
            else:
                mid.append(arr[i])
        mid.append(pivot)
        print(left,mid,right)
        return QuickSort(left)  + mid + QuickSort(right)
    else:
        return arr

def partition(arr, start, end):
    pivot = arr[start]
    left = start + 1
    right = end
    done = False
    while not done:
        while left <= right and arr[left] <= pivot:
            left += 1
        while left <= right and pivot <= arr[right]:
            right -= 1
        if right < left:
            done = True
        else:
            arr[left], arr[right] = arr[right], arr[left]
    arr[start], arr[right] = arr[right], arr[start]
    return right


def quick_sort(arr, start, end):
    if start < end:
        pivot = partition(arr, start, end)
        quick_sort(arr, start, pivot - 1)
        quick_sort(arr, pivot + 1, end)
    return arr

if __name__ == "__main__":
    RandArr = CreateRandArr(MaxNum=1000,ArrSize=10)
    #print(RandArr)
    print(quick_sort(RandArr,0,len(RandArr)-1))
