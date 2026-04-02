class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # [1,2,4,6]
        # prefix: [1,1,2,8]
        # postfix: [48, 24, 6, 1]
        # result: [48, 24, 12, 48]

        prefix = [1] * len(nums)
        postfix = [1] * len(nums)

        # prefix generating
        for i in range(1, len(nums)):
            prefix[i] = prefix[i - 1] * nums[i - 1]
        
        # postfix generating
        for i in range(len(nums) - 2, -1, - 1):
            postfix[i] = postfix[i + 1] * nums[i + 1]
        
        return [prefix[i] * postfix[i] for i in range(len(prefix))]



