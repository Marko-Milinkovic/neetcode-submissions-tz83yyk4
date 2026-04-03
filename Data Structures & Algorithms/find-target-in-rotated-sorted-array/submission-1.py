class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid

            # 1. Check if the LEFT side is sorted
            if nums[l] <= nums[mid]:
                # Is the target specifically in this sorted left range?
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            
            # 2. Otherwise, the RIGHT side MUST be sorted
            else:
                # Is the target specifically in this sorted right range?
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1

        return -1