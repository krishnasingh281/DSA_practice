def fourSum(nums, target):
    n = len(nums)
    st = set() # To store unique sorted quadruplets
    
    for i in range(n):
        for j in range(i + 1, n):
            hashset = set()
            for k in range(j + 1, n):
                # Calculate the required fourth value
                current_sum = nums[i] + nums[j] + nums[k]
                fourth = target - current_sum
                
                # If the fourth value exists in our hashset, we found a quadruplet
                if fourth in hashset:
                    # Create and sort the quadruplet to ensure uniqueness in the set
                    temp = sorted([nums[i], nums[j], nums[k], fourth])
                    st.add(tuple(temp)) # Sets in Python require hashable types like tuples
                
                # Add the current element to hashset for future lookups
                hashset.add(nums[k])
                
    # Convert the set of tuples back into a list of lists
    return [list(quad) for quad in st]