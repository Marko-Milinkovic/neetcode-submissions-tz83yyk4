# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        if root is None:
            return 0

        queue = deque([(root, 1)])

        result = 0
        while queue:

            cur , d = queue.popleft()

            if d > result:
                result = d

            if cur.left:
                queue.append((cur.left, d + 1))
            if cur.right:
                queue.append((cur.right, d + 1))
        
        return result