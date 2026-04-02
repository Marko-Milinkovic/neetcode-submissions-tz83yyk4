class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stack = [(root, float('-inf'), float('inf'))]  # (node, min_val, max_val)

        while stack:

            node, low, high = stack.pop()

            if not node:
                continue
            
            if (node.val <= low or node.val >= high):
                return False
            
            stack.append((node.left, low, node.val))
            stack.append((node.right, node.val, high))

        return True