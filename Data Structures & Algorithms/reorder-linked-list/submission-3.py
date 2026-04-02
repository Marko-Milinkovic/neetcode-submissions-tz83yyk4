# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        if not head:
            return None

        slow = fast = head
        prev = None
        while fast:
            prev = slow
            slow = slow.next
            if not fast.next:
                break
            fast = fast.next.next
        
        prev.next = None

        cur = slow
        prev = None
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        
        head1 = head
        head2 = prev

        while head2:
            temp1, temp2 = head1.next, head2.next

            head1.next = head2
            head2.next = temp1

            head1 = temp1
            head2 = temp2
        



