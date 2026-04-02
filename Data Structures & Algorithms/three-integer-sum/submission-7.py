class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        
        res = []
        nums.sort()


        for i in range(len(nums) - 1):

            l = i + 1
            r = len(nums) - 1

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            while l < r: 

                if nums[i] + nums[l] + nums[r] == 0:
                    res.append([nums[i], nums[l], nums[r]])

                    while l + 1 < len(nums) and nums[l + 1] == nums[l]:
                        l += 1
                    while r - 1 > 0 and nums[r - 1] == nums[r]:
                        r -= 1 
                
                if nums[i] + nums[l] + nums[r] < 0:
                    l += 1
                else:
                    r -= 1

        return res  














