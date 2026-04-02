class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dictionary = {}
        for i in range(len(nums)):
            if nums[i] in dictionary:
                return True
            else:
                dictionary[nums[i]] = 1
        return False