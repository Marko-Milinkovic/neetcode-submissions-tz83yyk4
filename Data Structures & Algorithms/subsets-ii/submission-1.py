class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        res = []
        stack = [([] , 0)]


        while stack:

            current , i = stack.pop()

            res.append(current)

            for j in range(i , len(nums)):
                if j > i and nums[j] == nums[j - 1]:
                    continue
                stack.append((current + [nums[j]] , j + 1))
        
        return res