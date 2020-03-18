import random

def CreateRandArr(MaxNum=100,ArrSize=10):
    arr = [random.randint(1,MaxNum) for i in range(ArrSize)]
    return arr 

def Swap(x,y):
        tmp = x
        x = y 
        y = tmp
        return x,y    

def TestArr():
    return [22,31,2,1,5,77,8,1230,212]

if __name__ == "__main__":
    print(CreateRandArr())