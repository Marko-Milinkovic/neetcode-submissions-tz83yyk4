# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        queue = [root]

        while queue:
            
            current = queue.pop(0)

            if current == None:
                continue

            if self.sameTree(current, subRoot):
                return True

            queue.append(current.right)
            queue.append(current.left)

        return False

    def sameTree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True

        stack = [(root, subRoot)]

        while stack:

            node1, node2 = stack.pop()

            if not node1 and not node2:
                continue

            if not node1 or not node2 or node1.val != node2.val:
                return False

            stack.append((node1.right, node2.right))
            stack.append((node1.left, node2.left))   

        return True






