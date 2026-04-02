class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        stack = [([], 0)]
        nums.sort()

        result = []
        
        while stack:
            current_subset, start = stack.pop()
            result.append(current_subset)

            for i in range(start, len(nums)):
                if i > start and nums[i-1] == nums[i]:
                    continue
                stack.append((current_subset + [nums[i]], i + 1))
        
        return result
                