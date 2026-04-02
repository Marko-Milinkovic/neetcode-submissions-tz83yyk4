class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        res = nums[0]

        while l <= r:
            # If the current segment is already sorted, 
            # nums[l] is the smallest in this range.
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
                
            mid = (l + r) // 2
            res = min(res, nums[mid])
            
            # If mid is part of the left sorted portion,
            # the minimum must be to the right.
            if nums[mid] >= nums[l]:
                l = mid + 1
            else:
                # Minimum is to the left
                r = mid - 1
                
        return res