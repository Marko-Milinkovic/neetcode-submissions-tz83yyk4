class Solution:
    def getSum(self, a: int, b: int) -> int:
        
        result = 0
        carry = 0

        for i in range(32):

            a_bit = (a >> i) & 1
            b_bit = (b >> i) & 1

            sum_bit = a_bit ^ b_bit ^ carry

             # Calculate new carry: at least 2 of the 3 bits are 1
            carry = (a_bit & b_bit) | (a_bit & carry) | (b_bit & carry)

            result |= (sum_bit << i)
        
        
        # Convert back to proper signed 32-bit integer
        # If the 32nd bit is 1, it's negative in two's complement
        if result & 0x80000000:  # Check if sign bit is set
            result -= 0x100000000  # Convert from unsigned to signed

        return result