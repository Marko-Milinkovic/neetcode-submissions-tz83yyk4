class Solution:
    def rob(self, nums: List[int]) -> int:
        
        temp = [0 for i in range(len(nums))]

        if len(nums) == 1:
            return nums[0]

        temp[0] = nums[0]
        temp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            temp[i] = max(temp[i-2] + nums[i], temp[i-1])
        
        return temp[-1]