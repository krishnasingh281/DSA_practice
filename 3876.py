class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        n = len(nums1)
        if n <= 1:
            return True
        odd_list = []
        for i in range(n):
            if nums1[i] % 2 != 0:
                odd_list.append(nums1[i])
        if len(odd_list)>=1:
            index = min(odd_list)
        else:
            return True
    
        odd_val = index

        for i in range(n):
            if nums1[i] % 2 == 0:
                nums1[i] = nums1[i] - odd_val

        for num in nums1:
            if num < 0:
                return False

        return True