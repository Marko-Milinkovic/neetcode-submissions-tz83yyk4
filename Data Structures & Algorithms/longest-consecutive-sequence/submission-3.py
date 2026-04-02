class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if not nums:
            return 0

        nums = sorted(nums)
        # 2, 3, 4, 4, 5, 10, 20

        res = 1
        cur = 1
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                continue
            if nums[i] + 1 == nums[i + 1]:
                cur += 1
            else:
                res = max(res, cur)
                cur = 1
        
        return max(res, cur)