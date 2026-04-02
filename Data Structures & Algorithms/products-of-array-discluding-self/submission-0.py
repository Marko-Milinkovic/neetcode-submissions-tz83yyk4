class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        # Step 1: Create arrays for left and right products
        left = [1] * n
        right = [1] * n
        output = [1] * n
        
        # Step 2: Fill left products
        for i in range(1, n):
            left[i] = left[i - 1] * nums[i - 1]
        
        # Step 3: Fill right products  
        for i in range(n - 2, -1, -1):
            right[i] = right[i + 1] * nums[i + 1]
        
        # Step 4: Multiply left and right products
        for i in range(n):
            output[i] = left[i] * right[i]
        
        return output