class Solution(object):
    def check(self, nums):
        maxi = 0
        for i in range(len(nums)):
            if nums[i] > maxi:
                maxi = i

        
        nums1 = nums[0:maxi+1]
        nums2 = nums[maxi+1:]

        for i in range(len(nums1)-1):
            if nums1[i] >= nums1[i+1]:
                return False
            
        for i in range(len(nums2)-1):
            if nums2[i] <= nums2[i+1]:
                return False       
        return True
    

nums = [1,1,1,1,1]
solution = Solution()   
result = solution.check(nums)
print(result)  # Output the result