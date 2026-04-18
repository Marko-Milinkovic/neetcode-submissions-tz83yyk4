class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0 # Buy pointer
        max_p = 0 # Global maximum profit

        for right in range(1, len(prices)):
            # If it's profitable, calculate profit and update max_p
            if prices[right] > prices[left]:
                current_profit = prices[right] - prices[left]
                max_p = max(max_p, current_profit)
            else:
                # If we found a price lower than our current buy price, 
                # move the buy pointer to this new minimum.
                left = right
        
        return max_p