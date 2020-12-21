maxNum = [-1,-1]
for i in range(9):
    num = int(input())
    if(i==0):
        maxNum[0] = num 
        maxNum[1] = i + 1 
    else:
        if(maxNum[0] < num):
            maxNum[0] = num 
            maxNum[1] = i + 1

print(maxNum)
