# https://ko.wikipedia.org/wiki/분할_정복_알고리즘 
# https://www.geeksforgeeks.org/divide-and-conquer-algorithm-introduction/
# https://www.geeksforgeeks.org/merge-sort/
import random
def mergeSort(arr): 
    if len(arr) >1: 
        mid = len(arr)//2 
        left = arr[:mid] 
        right = arr[mid:] 
  
        mergeSort(left) 
        mergeSort(right) 
  
        i = j = k = 0
          
        
        while i < len(left) and j < len(right): 
            if left[i] < right[j]: 
                arr[k] = left[i] 
                i+=1
            else: 
                arr[k] = right[j] 
                j+=1
            k+=1
          
        # Checking if any element was left 
        while i < len(left): 
            arr[k] = left[i] 
            i+=1
            k+=1
          
        while j < len(right): 
            arr[k] = right[j] 
            j+=1
            k+=1


arr = [12,1,20,15,152,2,7,92]
output = mergeSort(arr,0,len(arr))
print(output)

