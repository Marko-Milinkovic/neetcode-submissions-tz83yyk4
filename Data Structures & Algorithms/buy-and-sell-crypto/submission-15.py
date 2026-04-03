class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        profit = 0
        left = 0
        # I want to buy at lowest price, and sell at highest
        # Core Idea: move right to the newest found local minima
        for right in range(1, len(prices)):
            
            if prices[right] < prices[left]:
                left = right
            
            profit = max(profit, prices[right] - prices[left])
        
        return profit