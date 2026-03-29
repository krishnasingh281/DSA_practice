class Solution:
    def beautySum(self, s: str) -> int:
        sumu = 0
        n = len(s)
        
        for i in range(n):
            freq_map = {}
            
            for j in range(i, n):
                c = s[j]
                freq_map[c] = freq_map.get(c, 0) + 1

                if len(freq_map) > 1:
                    counts = freq_map.values()
                    sumu += max(counts) - min(counts)
                
        return sumu