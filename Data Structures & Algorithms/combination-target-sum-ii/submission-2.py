class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        nums = candidates
        nums.sort()

        stack = [([], 0)]

        result = []
        while stack:

            cur_result, cur_index = stack.pop()
            cur_sum = sum(cur_result)

            if cur_sum == target:
                result.append(cur_result)
            
            for i in range(cur_index, len(nums)):

                if i > cur_index and nums[i] == nums[i - 1]:
                    continue

                if cur_sum <= target:
                    stack.append((cur_result + [nums[i]], i + 1))
        
        return result
