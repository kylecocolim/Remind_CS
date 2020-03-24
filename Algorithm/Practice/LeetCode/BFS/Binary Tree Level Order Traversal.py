# Binary Tree Level Order Traversal With BFS
# 102 Binary Tree Level Order Traversal
# leetcode.com/problems/binary-tree-level-order-traversal/

class Node(object):
    def __init__(self,x):
        self.val = x 
        self.left =None 
        self.right = None 

class Solution(object):
    def levelOrder(self, root):
        level = []
        queue = []
        if root is None: return None
        if root.left == None and root.right == None:
            level.append([root.val])
            return level
        else:
            level.append([root.val])

            if root.left is not None:
                queue.append(root.left)
            if root.right is not None:
                queue.append(root.right)
            while queue:
                sub = []
                next_queue = []
                for i in range(len(queue)):
                   #Visit 
                   node = queue[i]
                   sub.append(node.val)
                   if node.left is not None:
                        next_queue.append(node.left)
                   if node.right is not None:
                        next_queue.append(node.right) 
                queue = next_queue
                level.append(sub)
        return level        
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        
arr = [1,2,2,3,4,4,3]
root = Node(3)
a = Node(9)
b = Node(20)
c = Node(15)
d = Node(7)
root.left = a 
root.right = b
b.left =c  
b.right =d 
root2= Node(1)
print(Solution().levelOrder(root2))