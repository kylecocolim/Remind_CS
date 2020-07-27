
# 인접 나무 같은 높이 금지
# k번째 나무는 
# 불가능 값 return -1

def solution(A):
    def isZigZag(treeSkyLine):
        direction = ''
        for idx in range(len(treeSkyLine)-1):
            if (treeSkyLine[idx+1] < treeSkyLine[idx]):
                if (direction == "Down"):
                    return False
                else:
                    direction = "Down"
            elif(treeSkyLine[idx+1] > treeSkyLine[idx]):
                if(direction == "UP"):
                    return False
                else:
                    direction = "UP"
            else:
                return False
        return True
    if(isZigZag(A) == True):
        return 0 
    else:
        cnt = 0
        for i in range(len(A)):
            CuttedtreeSkyLine = list(A)
            CuttedtreeSkyLine.pop(i)
            if (isZigZag(CuttedtreeSkyLine) == True):
                cnt +=1
        if cnt == 0:
            return -1
        else:
            return cnt

A = [3,4,5,3,7]
B = [1,3,1,2]
C = [1,2,3,4]

print(solution(B))