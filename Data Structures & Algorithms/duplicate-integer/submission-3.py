class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        dictionary = defaultdict(int)

        for num in nums:
            if dictionary[num] == 1:
                return True

            dictionary[num] = 1


        return False
