class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        total_subarray = 0

        prefix_sum = []
        curr_sum=0
        for n in nums:
            curr_sum+=n
            prefix_sum.append(curr_sum)
			
        counter = {}
        for curr_psum in prefix_sum:
            if curr_psum-k==0:
                total_subarray+=1
            if curr_psum-k in counter:
                total_subarray+=counter[curr_psum-k]
            if curr_psum in counter:
                counter[curr_psum]+=1
            else:
                counter[curr_psum]=1

        return total_subarray