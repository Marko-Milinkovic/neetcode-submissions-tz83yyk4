class Solution:

    def longestConsecutive(self, nums: List[int]) -> int:
        
        set_nums = set(nums)
        result = 0
        for num in set_nums:

            if (num - 1) not in set_nums: #crucial check
            #all numbers are visited maximum 2 times
                current_num = num
                current_length = 1

                while (current_num + 1 in set_nums):
                    #all numbers consumed in this loop will not be checked later
                    current_num += 1
                    current_length += 1

                result = max(result, current_length)

        return result        
