from collections import deque

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        queue = deque([root, None])  # None is used as a level separator
        height = 0

        while queue:
            curr = queue.popleft()

            if curr is None:
                height += 1
                # If there are still nodes to process, add another level marker
                if queue:
                    queue.append(None)
            else:
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)

        return height
