import itertools
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        arr1 = []
        arr2 = []

        for i in range(0,len(nums)):
            if nums[i]>0:
                arr1.append(nums[i])
            else:
                arr2.append(nums[i])
        
        arr3 = list(itertools.chain.from_iterable(zip(arr1, arr2)))
        return arr3