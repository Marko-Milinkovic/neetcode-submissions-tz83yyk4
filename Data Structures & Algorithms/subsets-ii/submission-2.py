class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        result = []
        stack = [([], 0)]

        while stack:

            cur_list, cur_index = stack.pop()
            result.append(cur_list)

            for i in range(cur_index, len(nums)):
                
                if i > cur_index and nums[i] == nums[i - 1]:
                    continue

                stack.append((cur_list + [nums[i]], i + 1))
        
        return result