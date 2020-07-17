# https://app.codility.com/programmers/lessons/3-time_complexity/frog_jmp/
import math
def FrogJmp(X,Y,D):
    if (X < Y):
        return math.ceil((Y-X)/D)
    else:
        return 0 


X = 10 
Y = 15
D = 30
print(FrogJmp(X,Y,D))