class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        stack = []
        for i in range(len(nums)):
            stack.append(([nums[i]], {i}))
        
        result = []
        while stack:

            cur_list, cur_set = stack.pop()
            if len(cur_list) == len(nums):
                result.append(cur_list)
                continue
            
            for i in range(len(nums)):

                if i not in cur_set:

                    new_list = cur_list + [nums[i]]
                    new_used = cur_set.copy()
                    new_used.add(i)

                    stack.append((new_list, new_used))
        
        return result




