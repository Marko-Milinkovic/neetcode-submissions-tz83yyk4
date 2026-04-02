class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        if not subRoot:
            return True
        if not root:
            return False

        stack = [root]

        while stack:
            current = stack.pop()

            if current.val == subRoot.val:
                stack2 = [(current, subRoot)]
                match = True  # assume match, disprove later

                while stack2:
                    a, b = stack2.pop()

                    if not a and not b:
                        continue
                    if not a or not b or a.val != b.val:
                        match = False
                        break

                    stack2.append((a.left, b.left))
                    stack2.append((a.right, b.right))

                if match:
                    return True  # we found subtree match!

            if current.left:
                stack.append(current.left)
            if current.right:
                stack.append(current.right)

        return False
