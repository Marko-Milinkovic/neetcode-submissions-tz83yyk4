from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        queue = deque([root])
        result = []

        while queue:
            
            level_size = len(queue)  # ← FIX: store level size BEFORE popping

            for i in range(level_size):
                current = queue.popleft()

                # now check against the FIXED level size, not changing queue length
                if i == level_size - 1:      # ← now correct
                    result.append(current.val)

                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)

        return result
