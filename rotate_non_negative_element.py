class Solution:
    def rotateElements(self, nums, k):
        d = {}
        for i in range(len(nums)):
            if nums[i]>=0:
                d[nums[i]] = i

        keys = list(d.keys())
        for i in range(len(keys)):
            new_index = (d[keys[i]] - k) % len(nums)
            d[keys[i]] = new_index
        
        for key in d:
            original_index = d[key]
            nums[original_index] = key
        return nums
    


