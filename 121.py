class Solution:
    def maxProfit(self, prices):
        mini = float('inf') 
        max_profit = 0 

        for price in prices:
            if price < mini:
                mini = price
            
            # 2. Calculate profit if we sold at current price
            current_profit = price - mini
            
            # 3. Keep the best profit we've seen
            if current_profit > max_profit:
                max_profit = current_profit
                
        return max_profit    