class Solution:
    def countBits(self, n: int) -> List[int]:
        
        result = [0] * (n + 1)
        power_of_2 = 1
        
        for i in range(1, n + 1):
            if power_of_2 * 2 == i:
                power_of_2 = i

            result[i] = 1 + result[i - power_of_2]
        
        return result