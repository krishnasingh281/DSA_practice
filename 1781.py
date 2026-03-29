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
    


    class Solution:
    def beautySum(self, s: str) -> int:
        def diff(substring):
            freq_map = {}
            
            for i in range(len(substring)):
                char = substring[i]
                if char in freq_map:
                    freq_map[char] += 1
                else:
                    freq_map[char] = 1

            return (max(freq_map.values()) - min(freq_map.values()))

        list1 = []

        for i in range(len(s)):
            for j in range(i, len(s)):
                substring = s[i : j + 1]
                list1.append(diff(substring))

        
        return sum(list1)
            
         