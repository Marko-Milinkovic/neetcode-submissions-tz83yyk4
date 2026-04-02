class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        nums = candidates

        nums.sort()

        result = []
        stack = [([] , 0)]

        while stack:

            current , i = stack.pop()
            s = sum(current)

            if s == target:
                result.append(current)

            for j in range(i, len(nums)):
                
                if j > i and nums[j] == nums[j - 1]: # protect from duplicate branches on same level
                    continue                         # that eventually produce same comb

                if nums[j] + s <= target:
                    stack.append((current + [nums[j]], j + 1)) # protect from duplicates

        return result 