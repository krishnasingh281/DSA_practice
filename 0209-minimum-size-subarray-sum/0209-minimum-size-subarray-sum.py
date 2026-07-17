class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        min_len = float('inf')
        current_sum = 0
        i = 0
        
        for j in range(n):
            current_sum += nums[j]
            
            while current_sum >= target:
                diff = j - i + 1
                if diff < min_len:
                    min_len = diff
                current_sum -= nums[i]
                i+= 1
                
        if min_len == float('inf'):
            return 0
            
        return min_len