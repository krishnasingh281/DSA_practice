class Solution(object):
    def twoSum(self, nums, target):
        indexed_nums = []
        for idx in range(len(nums)):
            indexed_nums.append([nums[idx], idx])
        

        indexed_nums.sort()
        
        i = 0
        j = len(nums) - 1

        while i < j:
            current_sum = indexed_nums[i][0] + indexed_nums[j][0]
            
            if current_sum == target:
                return [indexed_nums[i][1], indexed_nums[j][1]]
            elif current_sum > target:
                j -= 1
            else:
                i += 1
        return []