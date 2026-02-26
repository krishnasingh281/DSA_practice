class Solution(object):
    def moveZeroes(self, nums):
        for i in range(0,len(nums)):
            if nums[i] == 0:
                nums.append(0)
                nums.remove(0)

        return nums
    
