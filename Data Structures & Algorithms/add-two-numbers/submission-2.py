# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        cur1, cur2 = l1, l2
        carry = 0

        cur = dummy = ListNode()

        while cur1 or cur2 or carry:
            a = cur1.val if cur1 else 0
            b = cur2.val if cur2 else 0

            c = (a + b + carry) % 10
            carry = (a + b + carry) // 10

            cur.next = ListNode(c)
            cur = cur.next

            cur1 = cur1.next if cur1 else None
            cur2 = cur2.next if cur2 else None
        
        return dummy.next


