class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])

        temp = [0 for i in range(len(nums))]

        temp[0] = nums[0]
        temp[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            temp[i] = max(temp[i-1], nums[i] + temp[i-2])
        
        return temp[-1]