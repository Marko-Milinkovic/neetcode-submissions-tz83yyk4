class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        stack = [([] , 0)]
        
        result = []
        while stack:

            current , i = stack.pop()
            result.append(current)

            for j in range(i , len(nums)):
                
                if j > i and nums[j] == nums[j - 1]:
                    continue

                stack.append((current + [nums[j]], j + 1))
        
        return result