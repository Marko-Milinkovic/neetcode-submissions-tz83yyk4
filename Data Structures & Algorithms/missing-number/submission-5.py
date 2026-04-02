class Solution:
    def missingNumber(self, nums: List[int]) -> int:
    
        n = len(nums)

        # XOR all numbers from 0 to n
        xor_complete = 0
        for i in range(n + 1):  # 0, 1, 2, 3
            xor_complete ^= i
        
        # XOR all numbers in the array
        xor_array = 0
        for num in nums:        # 3, 0, 1
            xor_array ^= num
        
        # The difference is the missing number
        return xor_complete ^ xor_array