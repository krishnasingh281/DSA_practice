class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        def kadane(arr):
            tsum = 0
            max_sum = arr[0]

            for i in range(len(arr)):
                tsum += arr[i]
                max_sum = max(max_sum, tsum)

                if tsum < 0:
                    tsum = 0

            return max_sum

        positive_sum = kadane(nums)
        negative_sum = kadane([-j for j in nums])

        return max(positive_sum, negative_sum)