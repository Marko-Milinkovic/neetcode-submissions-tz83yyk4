class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        stack = []

        for num in nums:
            stack.append([num])
        
        result = []

        while stack:

            current_permutation = stack.pop()

            if len(current_permutation) == len(nums):
                result.append(current_permutation)

            for num in nums:
                if num not in current_permutation and len(current_permutation) < len(nums):
                    stack.append(current_permutation + [num])

        return result
        