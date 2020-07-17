# https://app.codility.com/programmers/lessons/2-arrays/odd_occurrences_in_array/

def OddOccurrencesInArray(A):
    oddDict = dict()
    for element in A:
        try:
           oddDict[element] +=1
        except:
            oddDict[element] = 1

    for key,value in oddDict.items():
        if(value % 2 == 1):
            return key
    return 0

A = [9,3,9,3,9,7,9]
print(OddOccurrencesInArray(A))