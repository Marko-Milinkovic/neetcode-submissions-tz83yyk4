class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # [3,4,5,6,7,1,2]


        l = 0
        r = len(nums) - 1

        while l <= r:

            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            
            # left half is sorted
            if nums[l] <= nums[mid]:
                # check if target is in left sorted half 
                if nums[l] <= target <= nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1

            # if left is not sorted, then right is sorted 
            else:
                # check if target is in right sorted half
                if nums[mid] <= target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1

        return - 1