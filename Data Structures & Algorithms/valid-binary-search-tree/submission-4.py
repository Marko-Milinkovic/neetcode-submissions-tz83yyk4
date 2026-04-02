class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stack = []
        prev = None

        while stack or root:
            # go to leftmost
            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()
            
            # check strictly increasing
            if prev is not None and root.val <= prev:
                return False

            prev = root.val
            root = root.right
        
        return True
