class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        left = 0
        right = 1
        result = 0

        while right < len(prices):
            profit = prices[right] - prices[left]
            if profit > result:
                result = profit

            if prices[right] <= prices[left]:
                left = right
            
            right += 1
        
        return result
