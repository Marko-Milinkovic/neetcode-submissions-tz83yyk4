# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        listSize = 0
        temp = head
        while temp:
            listSize += 1
            temp = temp.next

        if listSize == 1:
            return None
        
        if listSize == n:
            return head.next
        
        advance = listSize - n

        prev = None
        curr = head
        counter = 0
        while counter < advance:
            prev = curr
            curr = curr.next
            counter += 1

        prev.next = curr.next

        return head

