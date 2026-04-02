class Solution:
    def buildTree(self, preorder, inorder):
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])
        stack = [root]
        in_idx = 0

        for val in preorder[1:]:
            node = stack[-1]

            # Still building left side
            if node.val != inorder[in_idx]:
                node.left = TreeNode(val)
                stack.append(node.left)
            else:
                # Backtrack until mismatch
                while stack and stack[-1].val == inorder[in_idx]:
                    node = stack.pop()
                    in_idx += 1
                node.right = TreeNode(val)
                stack.append(node.right)

        return root
