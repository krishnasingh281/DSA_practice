import math

class Solution:
    def smallestDivisor(self, nums: list[int], threshold: int) -> int:
        # The maximum possible divisor is the largest number in the array
        max_val = max(nums)
        
        # Iterate d from 1 to max(nums)
        for d in range(1, max_val + 1):
            total_sum = 0
            
            # Calculate the sum of ceil(nums[i] / d)
            for i in range(len(nums)):
                total_sum += math.ceil(nums[i] / d)
            
            # If the sum meets the threshold, return the divisor d
            if total_sum <= threshold:
                return d
                
        return -1