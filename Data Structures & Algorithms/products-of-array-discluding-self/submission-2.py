class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        right = [1 for i in range(len(nums))]
        left = [1 for i in range(len(nums))]

        #right[-1] = nums[len(nums) -1]
        for i in range(len(nums) - 2, -1, -1):
            right[i] = right[i + 1] * nums[i + 1]
        
        print(right)
        
        #left[0] = nums[0]
        for i in range(1, len(nums)):
            left[i] = left[i - 1] * nums[i - 1]
        
        result = []
        for i in range(len(nums)):
            result.append(left[i] * right[i])

        return result