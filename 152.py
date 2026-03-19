class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        maxi = mini = 1

        for i in nums:
            temp = maxi * i
            maxi = max(temp, mini * i, i)
            mini = min(temp, mini * i, i)

            res = max(res, maxi)
        
        return res