class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        res = nums[0]

        while l <= r:
            # If the current segment is already sorted, 
            # the minimum in this segment is nums[l].
            # We return the best between our global 'res' and this 'nums[l]'.
            if nums[l] <= nums[r]:
                return min(res, nums[l])

            mid = (l + r) // 2
            res = min(res, nums[mid])
            
            # Use mid vs l to decide which side is the 'continuous' sorted half
            if nums[mid] >= nums[l]:
                # Left side is sorted, so the rotation/inflection 
                # point must be on the right.
                l = mid + 1
            else:
                # Right side is sorted, so the rotation/inflection
                # point must be on the left.
                r = mid - 1
        
        return res