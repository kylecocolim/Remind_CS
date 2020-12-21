# https://leetcode.com/problems/add-two-numbers/
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num = 0
        num2 = 0
        index = 1
        while(l1):
            num += index * l1.val
            index *= 10
            l1 = l1.next
        index = 1
        while(l2):
            num2 += index * l2.val
            index *= 10
            l2 = l2.next
        resultNum  = str(num + num2)
        print(resultNum)
        resultNode = head = ListNode()
        if(len(resultNum)>0):
            resultNode.val = resultNum[-1]
            if(len(resultNum) > 1):
                for i in range(1,len(resultNum)):
                    newNode = ListNode(resultNum[len(resultNum) - i - 1])
                    resultNode.next = newNode
                    resultNode = resultNode.next
        return head
        