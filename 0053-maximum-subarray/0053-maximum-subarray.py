class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi = nums[0]
        cur_sum = 0
        for i in range(len(nums)):
            cur_sum = max(nums[i], cur_sum + nums[i])
            maxi = max(maxi, cur_sum)
        return maxi
