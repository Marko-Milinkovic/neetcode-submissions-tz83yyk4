# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        stack = [(p, q)]

        while stack:

            temp1, temp2 = stack.pop();

            if not temp1 and not temp2:
                continue
            if not temp1 or not temp2 or temp1.val != temp2.val:
                return False
            
            stack.append((temp1.right, temp2.right))
            stack.append((temp1.left, temp2.left))

        return True
            
            





