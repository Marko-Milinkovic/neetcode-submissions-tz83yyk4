class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        stack = [(0, [], 0)]  

        while stack:

            start, path, total = stack.pop()

            if total == target:
                res.append(path)
            
            for i in range(start, len(nums)):
                val = nums[i]
                if val + total > target:
                    break
                stack.append((i, path + [val], val + total))
        
        return res
