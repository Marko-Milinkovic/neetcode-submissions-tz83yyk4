# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        if not head:
            return None

        cur = head
        length = 0
        while cur:
            cur = cur.next
            length += 1

        if length == n:
            head = head.next
            return head

        removeIndex = length - n

        cnt = 0
        cur = head
        prev = None
        while cur:
            
            if cnt == removeIndex:
                prev.next = cur.next
                return head
            
            prev = cur
            cur = cur.next
            cnt += 1
        
        


