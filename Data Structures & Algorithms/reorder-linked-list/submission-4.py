# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        original_head = p = q = head

        while q and q.next:

            p = p.next
            q = q.next.next
        
        
        cur = p.next
        p.next = None

        prev = None

        while cur:

            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        
        reversed_head = prev

        while reversed_head:

            temp1 = original_head.next
            temp2 = reversed_head.next

            original_head.next = reversed_head
            reversed_head.next = temp1

            original_head = temp1
            reversed_head = temp2
        
        

