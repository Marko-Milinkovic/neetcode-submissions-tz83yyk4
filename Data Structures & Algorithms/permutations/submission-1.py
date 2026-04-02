class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        stack = []
        for num in nums:
            stack.append([num])

        result = []
        while stack:
            current = stack.pop()

            if len(current) == len(nums):
                result.append(current)
            else:
                for num in nums:
                    if num not in current:
                        stack.append(current + [num])
        
        return result
