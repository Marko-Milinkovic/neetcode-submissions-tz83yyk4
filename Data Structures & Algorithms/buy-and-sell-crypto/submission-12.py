class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        current_min_price = prices[0]
        profit = 0

        for price in prices:

            current_min_price = min(current_min_price, price)
            profit = max(profit, price - current_min_price)
        
        return profit