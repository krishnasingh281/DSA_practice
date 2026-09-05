class Solution:
    def findDisappearedNumbers(self, nums: list[int], lower: int, upper: int) -> list[list[int]]:
        nums_set = set(nums)
        start = lower
        ans = []

        for end in range(lower, upper + 1):
            if end in nums_set:
                if start != end:
                    ans.append([start, end - 1])
                start = end + 1
            elif end == upper:
                ans.append([start, end])
        return ans