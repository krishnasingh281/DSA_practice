class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        #1
        cur_sum_no_del = cur_sum_del = max_sum = arr[0]
        #2 
        for num in arr[1:]:
            #3
            cur_sum_del = max(cur_sum_del + num, num, cur_sum_no_del)
            #4
            cur_sum_no_del = max(cur_sum_no_del + num, num)
            #5
            max_sum = max(max_sum, cur_sum_no_del, cur_sum_del)
        #6
        return max_sum