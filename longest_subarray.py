def longestSubarrayWithSumK(a, k):
    preSumMap = {}
    current_sum = 0
    maxLen = 0
    
    for i in range(len(a)):
        current_sum += a[i]
        
        # Case 1: The sum from the beginning equals k
        if current_sum == k:
            maxLen = max(maxLen, i + 1)
        
        # Case 2: Check if (sum - k) exists in our map
        rem = current_sum - k
        if rem in preSumMap:
            length = i - preSumMap[rem]
            maxLen = max(maxLen, length)
        
        # Case 3: Only add sum to map if it doesn't exist 
        # (This ensures we keep the leftmost index for maximum length)
        if current_sum not in preSumMap:
            preSumMap[current_sum] = i
            
    return maxLen