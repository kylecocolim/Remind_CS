# https://app.codility.com/programmers/lessons/1-iterations/binary_gap/
a = 66561
b = "{0:b}".format(a)
result = 0
print(b)
cntFlag = False
cnt = 0
# What is Next Number is 0
for i in range(0,len(b)):
    if(cntFlag == True and b[i] == '1'):
        cntFlag = False 
        result = max(result, cnt)
        cnt = 0
    if(cntFlag == False and b[i] == '1'):
        cntFlag = True 
    if(cntFlag == True and b[i] == '0'):
        cnt +=1

print(result)