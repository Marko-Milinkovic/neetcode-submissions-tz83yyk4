from collections import defaultdict
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        dictionary = defaultdict(int)

        for i in range(len(nums)):
            if dictionary[nums[i]] == 1:
                return True
            else:
                dictionary[nums[i]] += 1

        return False