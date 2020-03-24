 #https://leetcode.com/problems/rotate-list/


#for i in range(0,len(arr)):
 #   arr[i] = tmp[(i+k)%len(arr)]
 #   tmp.append(arr[(i-k)%len(arr)])
    

class ListNode(object):
    def __init__(self, x):
        self.val = x     
        self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        root = ListNode(None)
        root.next = head
        arr = [] 
        while head is not None:
            arr.append(head.val)
            head = head.next
        head = root.next
        cnt = 0
        while head is not None:
                head.val = arr[(cnt-k)%len(arr)]
                head = head.next
                cnt +=1
        return root.next

# Test Code # 
arr = [1,2,3,4,5]
k = 2
head = ListNode(1)
Node = ListNode(2)
Node2 = ListNode(3)
Node3 = ListNode(4)
Node4 = ListNode(5)
head.next= Node
Node.next= Node2
Node2.next = Node3
Node3.next = Node4 
head = Solution().rotateRight(head,k)
print(head.val)