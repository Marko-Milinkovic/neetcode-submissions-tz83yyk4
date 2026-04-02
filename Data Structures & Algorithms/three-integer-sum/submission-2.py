class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        

        result = []

        nums.sort()

        for i in range(len(nums)):

            pivot = nums[i]

            if i > 0 and nums[i] == nums[i-1]:
                continue  # skip duplicate pivots


            p = i + 1
            q = len(nums) - 1

            while p < q:

                if nums[p] + nums[q] + pivot == 0:
                    result.append([pivot, nums[p], nums[q]])
                    p += 1
                    q -= 1

                    # skip duplicates
                    while p < q and nums[p] == nums[p-1]:
                        p += 1
                    while p < q and nums[q] == nums[q+1]:
                        q -= 1
                
                if nums[p] + nums[q] + pivot > 0:
                    q -= 1
                
                if nums[p] + nums[q] + pivot < 0:
                    p += 1
            
        return result









