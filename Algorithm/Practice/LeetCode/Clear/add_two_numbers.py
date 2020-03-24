class ListNode:
    def __init__(self,x):
        self.val = x 
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        tmp = int()
        head = l1
        while(l1 is not None or l2 is not None):
            if tmp is not None:
                l1.val += tmp
                tmp = None
            
            l1.val = l1.val + l2.val
            if l1.val>=10:
                l1.val %= 10
                tmp = 1
            print(l1.val)
            if l1.next == None and tmp ==1:
                addNode = ListNode(tmp)
                l1.next = addNode
                break
            l1 = l1.next
            l2 = l2.next
        
        return head.next
l1 = ListNode(1)
l1_1 =ListNode(8)
#l1_2 = ListNode(3)

l2 = ListNode(0)
#l2_1 = ListNode(6)
#l2_2 = ListNode(9)

# Link
l1.next = l1_1 
#l1_1.next = l1_2 

#l2.next = l2_1 
#l2_1.next = l2_2

Solution().addTwoNumbers(l1,l2)