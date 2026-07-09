class Solution:
    def check(self, nums: List[int]) -> bool:
        index = -1
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                index = i
                break
        
        if index == -1:
            return True
            
        decide = True
        for i in range(index + 1, len(nums) - 1):
            if nums[i] > nums[i + 1]:
                decide = False
                break
                
        if decide and nums[-1] <= nums[0]:
            return True
        else:
            return False