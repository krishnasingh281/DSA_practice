class Solution:
    def countCommas(self, n: int) -> int:
        commas = 0
        m = 1000
        
        while n >= m:
            commas += (n - m + 1)
            m *= 1000
            
        return commas