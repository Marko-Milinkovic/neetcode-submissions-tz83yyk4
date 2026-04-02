class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        result = []

        stack = [([], 0)]

        while stack:

            current, i = stack.pop()
            current_sum = sum(current)

            if current_sum == target:
                result.append(current)
            else:

                for j in range(i , len(nums)):
                    if current_sum + nums[j] <= target:
                        stack.append((current + [nums[j]], j))
        
        return result