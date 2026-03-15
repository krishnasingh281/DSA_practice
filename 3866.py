class Solution:
    def firstUniqueEven(self, nums: list[int]) -> int:
        no = []
        freq_map = {}
        
        for x in nums:
            if x % 2 == 0:
                no.append(x)

        for x in no:
            if x in freq_map:
                freq_map[x] += 1
            else:
                freq_map[x] = 1

        for x in no:
            if freq_map[x] == 1:
                return x

        return -1