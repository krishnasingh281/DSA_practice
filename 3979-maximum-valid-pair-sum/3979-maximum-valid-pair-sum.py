class Solution:
    def maxValidPairSum(self, nums: list[int], k: int) -> int:
        maxi=nums[0]
        res=0
        for i in range(k,len(nums)):
            maxi=max(maxi,nums[i-k])
            res=max(res,maxi+nums[i])
        return res