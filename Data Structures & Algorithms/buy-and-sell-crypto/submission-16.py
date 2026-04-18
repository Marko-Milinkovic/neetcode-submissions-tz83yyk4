class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # max_profit = highest_seen_so_far - lowest_seen_so_far

        lowest = 1000
        highest = -1

        buy = sell = 0
        result = 0

        for i in range(len(prices)):

            if prices[i] < lowest:
                lowest = prices[i]
                buy  = i
            
            if prices[i] > highest:
                highest = prices[i]
                sell = i
            
            if sell < buy:
                sell = buy
                highest = prices[buy]
            
            result = max(result, prices[sell] - prices[buy])

        return result