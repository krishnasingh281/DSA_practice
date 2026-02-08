class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n = len(nums)
        ind = -1

        # 1. Find the "pivot" index
        # This is the first index from the right where nums[i] < nums[i+1]
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                ind = i
                break

        # 2. If no pivot is found, the array is in descending order
        # Just reverse it to get the smallest possible permutation
        if ind == -1:
            nums.reverse()
            return

        # 3. Find the smallest number larger than nums[ind] to its right
        for i in range(n - 1, ind, -1):
            if nums[i] > nums[ind]:
                nums[i], nums[ind] = nums[ind], nums[i]
                break

        # 4. Reverse the sub-array to the right of the pivot
        # Python slice assignment makes this easy:
        nums[ind + 1:] = reversed(nums[ind + 1:])