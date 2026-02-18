class Solution:
    def majorityElement(self, nums):
        nos = len(nums)//3
        freq_map = {}
        arr = []
        for i in range(len(nums)):
            if nums[i] in freq_map:
                freq_map[nums[i]]+=1
            else:
                freq_map[nums[i]]=1
        for key, count in freq_map.items():
            if count > nos:
                arr.append(key)
        return arr