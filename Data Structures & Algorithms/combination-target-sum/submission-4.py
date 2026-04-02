class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        stack = [([], 0)]
        nums.sort()

        result = []
        while stack:

            current , i = stack.pop()

            s = sum(current)
            if s == target:
                result.append(current)
            
            for j in range(i , len(nums)):
                if j > i and nums[j] == nums[j - 1]: # no duplicate branches on same level
                    continue
                if s + nums[j] <= target:
                    stack.append((current + [nums[j]] , j)) # no duplicates in combination

        return result

