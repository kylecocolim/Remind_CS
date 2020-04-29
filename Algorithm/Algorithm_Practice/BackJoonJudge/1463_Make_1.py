def Make_1(num):
    arr = [int() for i in range(num+1)]
    for i in range(2,len(arr)):
        arr[i] = arr[i-1] + 1
        if (i%2 ==0):
            arr[i] = min(arr[i],arr[int(i/2)]+1)
        if (i%3 ==0):
            arr[i] = min(arr[i],arr[int(i/3)]+1)
        
    return arr[num]

    

check = input()
print(Make_1(int(check)))