from typing import List

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        
        def can_split(max_sum):
            subarrays = 1
            current_sum = 0
            
            for num in nums:
                if current_sum + num <= max_sum:
                    current_sum += num
                else:
                    subarrays += 1
                    current_sum = num
                    
            return subarrays <= k
        
        low = max(nums)      # minimum possible answer
        high = sum(nums)     # maximum possible answer
        
        while low <= high:
            mid = (low + high) // 2
            
            if can_split(mid):
                high = mid - 1
            else:
                low = mid + 1  
                
        return low