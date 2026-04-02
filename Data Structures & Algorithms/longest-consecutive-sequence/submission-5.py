class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums:
            return 0
        
        s = set(nums)
        result = 0

        for num in nums:

            if (num - 1) not in nums:
                temp = 1
                current = num
                while True:
                    if (current + 1) in s:
                        temp += 1
                        current = current + 1
                    else:
                        break
                
                if temp > result:
                    result = temp
        
        return result






