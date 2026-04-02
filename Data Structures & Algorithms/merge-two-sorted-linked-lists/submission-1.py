# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        

        res = dummy = ListNode()

        p = list1
        q = list2

        while p and q:

            if p.val < q.val:

                dummy.next = p
                p = p.next

            else:

                dummy.next = q
                q = q.next
            
            dummy = dummy.next

        dummy.next = p or q

        return res.next
