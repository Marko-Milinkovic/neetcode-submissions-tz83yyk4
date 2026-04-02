# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        queue = deque([root])

        while queue:
            cur = queue.popleft()

            if cur.val == subRoot.val:
                temp_queue = deque([(cur, subRoot)])
                flag = 1
                while temp_queue:
                    temp1, temp2 = temp_queue.popleft()

                    if not temp1 and not temp2:
                        continue
                    if not temp1 or not temp2:
                        flag = 0
                        continue
                    if temp1.val != temp2.val:
                        flag = 0

                    temp_queue.append((temp1.left, temp2.left))
                    temp_queue.append((temp1.right, temp2.right))

                if flag:
                    return True        

            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)
            
        return False
