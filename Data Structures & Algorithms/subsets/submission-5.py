class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        stack = [([] , 0)]
        
        result = []
        while stack:

            current , i = stack.pop()
            result.append(current)

            for j in range(i , len(nums)):
                
                

                stack.append((current + [nums[j]], j + 1))
        
        return result