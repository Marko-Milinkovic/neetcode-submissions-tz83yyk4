from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []
        
        result = []
        temp = []
        
        queue = deque([root, None])   # None is our sentinel marker
        
        while queue:
            node = queue.popleft()
            
            if node is None:
                result.append(temp)
                temp = []
                
                if queue:             # only add sentinel if there are nodes left
                    queue.append(None)
            else:
                temp.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return result
