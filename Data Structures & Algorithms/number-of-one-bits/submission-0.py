class Solution:
    def hammingWeight(self, n: int) -> int:
        
        num = n
        mask = 1
        result = 0
        
        for i in range(32):
            
            temp = num & mask
            if (temp):
                result += 1
            num = num >> 1
        
        return result