class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        # -1, 0, 1, 2, -1, -4

        nums = sorted(nums)
        # -4, -1, -1, 0, 1, 2

        for i in range(len(nums)):

            if i > 0 and nums[i] == nums[i - 1]:  
                continue  # skip duplicate i

            p = i + 1
            q = len(nums) - 1

            while p < q:

                if nums[i] + nums[p] + nums[q] == 0:
                    res.append([nums[i], nums[p], nums[q]])
                    p += 1
                    q -= 1

                    while p < q and nums[p] == nums[p - 1]:
                        p += 1
                    
                    while p < q and nums[q] == nums[q + 1]:
                        q -= 1
                
                elif nums[i] + nums[p] + nums[q] < 0:
                    p += 1
                
                elif nums[i] + nums[p] + nums[q] > 0:
                    q -= 1
        
        return res












