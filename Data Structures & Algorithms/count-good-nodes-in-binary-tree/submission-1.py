# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        queue = deque([(root, root.val)])

        result = 0
        while queue:

            node , cur_max = queue.popleft()

            if node.val >= cur_max:
                result += 1

            new_max = max(cur_max, node.val)
            
            if node.left:
                queue.append((node.left, new_max))
            if node.right:
                queue.append((node.right, new_max))
        
        return result
