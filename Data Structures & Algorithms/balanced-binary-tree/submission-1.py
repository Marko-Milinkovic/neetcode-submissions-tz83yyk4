class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        stack = [(root, False, 0)]  # node, visited_flag, height
        
        while stack:
            node, visited, height = stack.pop()
            
            if not node:
                continue
            
            if not visited:
                # Push self back as visited
                stack.append((node, True, 0))
                # Push children (not visited yet)
                stack.append((node.left, False, 0))
                stack.append((node.right, False, 0))
            
            else:
                # Children have already been visited — their heights are on stack below, 
                # BUT we cannot pop them. Instead, we recompute using recursion logic
                # since both children heights were already computed in earlier iterations.

                # We need children's heights which have been computed already:
                lh = node.left.height if node.left else 0
                rh = node.right.height if node.right else 0

                if abs(lh - rh) > 1:
                    return False

                # store height on the node itself temporarily
                node.height = 1 + max(lh, rh)

        return True
