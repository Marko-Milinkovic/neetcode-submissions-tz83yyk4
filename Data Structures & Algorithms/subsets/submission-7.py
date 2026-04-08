class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        stack = [([], 0)]
        result = []

        while stack:

            cur_list, cur_index = stack.pop()
            result.append(cur_list)

            for i in range(cur_index, len(nums)):

                new_list = cur_list + [nums[i]]
                stack.append((new_list, i + 1))

        return result

