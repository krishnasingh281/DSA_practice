class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        d = defaultdict(list)
        for i, v in enumerate(nums):
            d[v].append(i)
        return sum(l[1] - l[0] == l[2] - l[1] for l in d.values() if len(l) == 3)