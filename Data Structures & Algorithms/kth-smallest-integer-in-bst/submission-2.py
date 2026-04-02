class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        
        while True:
            # Go as left as possible
            while root:
                stack.append(root)
                root = root.left
            
            # Pop the next smallest
            root = stack.pop()
            k -= 1
            
            if k == 0:
                return root.val
            
            # Move to the right subtree
            root = root.right
