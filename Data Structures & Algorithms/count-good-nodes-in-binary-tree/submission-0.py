class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        stack = [(root, root.val)]
        res = 0

        while stack:
            node, maxValue = stack.pop()

            # check current node
            if node.val >= maxValue:
                res += 1

            # push children
            if node.right:
                stack.append((node.right, max(maxValue, node.val)))
            if node.left:
                stack.append((node.left, max(maxValue, node.val)))

        return res
