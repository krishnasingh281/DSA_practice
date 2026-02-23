class Solution:
    def longestBalanced(self, nums):
        max_len = 0
        n = len(nums)
        
        for i in range(n):
            distinct_evens = set()
            distinct_odds = set()
            
            for j in range(i, n):
                if nums[j] % 2 == 0:
                    distinct_evens.add(nums[j])
                else:
                    distinct_odds.add(nums[j])

                if len(distinct_evens) == len(distinct_odds):
                    current_len = j - i + 1
                    max_len = max(max_len, current_len)
                    
        return max_len