class Solution:
    def reverseBits(self, n: int) -> int:
        
        result = 0

        for i in range(32):

            current_bit = (n >> i) & 1
            result = result | ( current_bit << (31 - i))

        return result