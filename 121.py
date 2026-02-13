class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        mini = float('inf') # Start with a very high number
        max_profit = 0      # Track the best profit found so far

        for price in prices:
            # 1. Update the minimum price seen so far
            if price < mini:
                mini = price
            
            # 2. Calculate profit if we sold at current price
            current_profit = price - mini
            
            # 3. Keep the best profit we've seen
            if current_profit > max_profit:
                max_profit = current_profit
                
        return max_profit    