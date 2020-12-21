# https://leetcode.com/problems/merge-k-sorted-lists/

class ListNode:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next 

class Solution:
    def mergeKLists(lists):
        results = []
        for node in lists:
            while node:
                results.append(node.val)
                node = node.next
        
        return sorted(results)
n1 = ListNode(val= 1)
n2 = ListNode(val=4)
n3 = ListNode(val=5)
n1.next = n2
n2.next = n3 
k1 = ListNode(val=1)
k2 = ListNode(val=3)
k3 = ListNode(val=4)
k1.next = k2 
k2.next = k3 

lists = [n1,k1]
print(Solution.mergeKLists(lists))