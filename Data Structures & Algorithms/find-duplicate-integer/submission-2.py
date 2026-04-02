class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        # Phase 1: Find intersection point
        slow = nums[0]
        fast = nums[0]

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        # Phase 2: Find cycle entry (duplicate value)
        slow2 = nums[0]
        while slow != slow2:
            slow = nums[slow]
            slow2 = nums[slow2]
        
        return slow

'''

Floyd’s Tortoise and Hare cycle detection algorithm

# Phase 1 - finding meeting point
while slow != fast:
    slow = slow.next
    fast = fast.next.next

After Phase 1, 
the meeting point is exactly the same number of steps from the cycle start as the head is.

# Phase 2
slow2 = head
while slow != slow2:
    slow = slow.next
    slow2 = slow2.next

return slow  # start of cycle

head
 ↓
[---- X steps ----]  (before the cycle)

           cycle entry
                ↓
                o → o → o → o 
                    ↑       ↓
                    └───────┘
                      ↑
                      slow after phase 1 (also X steps ahead inside the cycle)


'''
