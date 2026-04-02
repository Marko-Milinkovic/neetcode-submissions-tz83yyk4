# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        p1 = p2 = head

        while p2.next:
            p1 = p1.next
            p2 = p2.next.next
            if p2 == None:
                break

        second_half = p1.next
        p1.next = None

        prev = None
        curr = second_half

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        first = head
        second = prev

        while second:
            temp1 = first.next
            temp2 = second.next

            first.next = second
            second.next = temp1

            first = temp1
            second = temp2
    












