# https://www.acmicpc.net/problem/9095
class Adding():
    def __init__(self,testcases,target):
        self.count= 0
        self.testcases = int(testcases)
        self.target = target
    def function(self):
        def recursion(number,target):
            if number > target : 
                return 0
            if number == target:
                self.count += 1
                return True
            recursion(number + 1,target)
            recursion(number + 2,target)
            recursion(number + 3,target)
        answer = []
        for test in range(self.testcases):
            # Each Target Solution
            recursion(1,self.target[test])
            recursion(2,self.target[test])
            recursion(3,self.target[test])

            print(self.count)
            self.count = 0
# 1. Number Switch
# 1 -> 2 -> 3
# 


#testcases = 3
#arr = [4,7,10]
testcases = input()
arr = [ int(input()) for i in range(int(testcases))]
Adding(testcases,arr).function()
