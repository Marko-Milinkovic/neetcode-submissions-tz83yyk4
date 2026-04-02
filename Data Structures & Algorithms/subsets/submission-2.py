class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        stack = [([], 0)]
        result = []

        while stack:
            curr, i = stack.pop()
            result.append(curr)

            for j in range(i, len(nums)):
                if j > 0 and nums[j] == nums[j - 1]:
                    continue
                stack.append((curr + [nums[j]], j + 1))

        return result

        