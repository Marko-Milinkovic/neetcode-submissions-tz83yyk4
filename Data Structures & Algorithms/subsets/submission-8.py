class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # Stack stores (current_subset, index_of_last_element_added)
        # We start index at -1 so the first loop can pick index 0
        stack = [([], -1)] 
        result = []

        while stack:
            cur_list, last_idx = stack.pop()
            result.append(cur_list)

            for i in range(len(nums)):
                # 1. 'nums[i] not in cur_list' ensures we don't pick the same value twice 
                # 2. 'i > last_idx' ensures we only pick elements to the RIGHT
                #    This is what prevents [2,1] if we already have [1,2]
                if nums[i] not in cur_list and i > last_idx:
                    new_subset = cur_list + [nums[i]]
                    stack.append((new_subset, i))

        return result