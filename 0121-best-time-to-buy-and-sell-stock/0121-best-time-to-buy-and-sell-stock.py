class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        mini = float('inf') 
        max_profit = 0      

        for price in prices:
            if price < mini:
                mini = price
            
            current_profit = price - mini
            
            if current_profit > max_profit:
                max_profit = current_profit
                
        return max_profit