from collections import defaultdict
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        dictionary = defaultdict(int)

        for i in range(len(nums)):
            dictionary[nums[i]] += 1
        
        for i in range(len(nums)+1):
            if not dictionary[i]:
                return i


