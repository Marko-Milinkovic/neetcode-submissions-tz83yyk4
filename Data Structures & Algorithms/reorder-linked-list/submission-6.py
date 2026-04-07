# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        
        second_half = slow.next
        slow.next = None

        prev = None
        cur = second_half

        while cur:

            temp = cur.next
            cur.next = prev

            prev = cur
            cur = temp
    
        second_half = prev
        first_half = head

        while first_half and second_half:

            temp1 = first_half.next
            temp2 = second_half.next

            first_half.next = second_half
            second_half.next = temp1

            first_half = temp1
            second_half = temp2
        

            



