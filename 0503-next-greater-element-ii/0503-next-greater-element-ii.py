class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [-1] * n
        st = []

        for i in range(2 * n):
            x = nums[i % n]
            while st and nums[st[-1]] < x:
                res[st.pop()] = x
            if i < n:
                st.append(i)

        return res