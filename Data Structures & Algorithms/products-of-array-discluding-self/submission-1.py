class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        right = [1] * n
        left = [1] * n

        for i in range(n - 1, -1, - 1):
            if i == n - 1:
                continue
            right[i] = right[i+1] * nums[i + 1]
        
        for i in range(n):
            if i == 0:
                continue
            left[i] = left[i-1] * nums[i-1]

        print(right)
        print(left)

        result = [0] * n
        for i in range(n):
            result[i] = left[i] * right[i]

        return result