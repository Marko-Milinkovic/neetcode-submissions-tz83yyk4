class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 1. Create a dummy node pointing to head
        dummy = ListNode(0, head)
        
        # 2. Get the total length
        l = 0
        cur = head
        while cur:
            l += 1
            cur = cur.next
        
        # 3. Find the node BEFORE the one we want to delete
        # The node to remove is at index (l - n)
        # We want to stop at (l - n) steps starting from dummy
        target_steps = l - n
        prev = dummy
        for _ in range(target_steps):
            prev = prev.next
            
        # 4. Skip the target node
        prev.next = prev.next.next
        
        # 5. Return the REAL head (dummy.next)
        return dummy.next