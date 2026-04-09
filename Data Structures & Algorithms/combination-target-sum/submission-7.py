class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        stack = [([], 0)]
        result = []

        while stack:

            cur_result, cur_index = stack.pop()
            cur_sum = sum(cur_result)

            if cur_sum == target:
                result.append(cur_result)
                continue

            for i in range(cur_index, len(nums)):
                if cur_sum + nums[i] <= target:
                    stack.append((cur_result + [nums[i]] , i))

        return result 



