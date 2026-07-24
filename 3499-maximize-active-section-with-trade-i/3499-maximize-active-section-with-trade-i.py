class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        blocks = []
        i = 0
        n = len(s)

        while i < n:
            j = i
            while j < n and s[i] == s[j]:
                j += 1

            length = j - i if s[i] == '1' else -(j - i)
            blocks.append(length)
            i = j
        
        prev_zero = max_zero = -1
        cnt_ones = 0

        for block in blocks:
            if block > 0:
                cnt_ones += block
                continue
            
            if prev_zero != -1:
                max_zero = max(max_zero, prev_zero + -block)

            prev_zero = -block
        
        return max(cnt_ones, cnt_ones + max_zero)