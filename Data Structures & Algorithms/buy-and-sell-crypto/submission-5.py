class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        result = 0
        left = 0

        for right in range(len(prices)):
            
            current_profit = prices[right] - prices[left]
            if (result < current_profit):
                result = current_profit

            if (prices[left] > prices[right]):
                left = right
        
        return result