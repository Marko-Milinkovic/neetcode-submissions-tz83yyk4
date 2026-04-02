class Solution:
    def climbStairs(self, n: int) -> int:
        
        result = [1 for i in range(n + 1)]

        for i in range(n - 2, -1, -1):
            result[i] = result[i+1] + result[i+2]
        
        return result[0]
