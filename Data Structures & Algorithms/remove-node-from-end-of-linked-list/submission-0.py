# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        temp = head
        nodes = []
        while temp:
            nodes.append(temp)
            temp = temp.next
        
        length = len(nodes)

        remove_index = length - n

        if remove_index == 0:
            return head.next

        nodes[remove_index-1].next = nodes[remove_index].next

        return head





