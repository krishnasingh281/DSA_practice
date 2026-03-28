class Solution:
    def romanToInt(self, s: str) -> int:
        freq_map = {'I':1,
                   'V':5,
                   'X':10,
                   'L':50,
                   'C':100,
                   'D':500,
                   'M':1000}
        list1 = list(s)
        total= 0

        for i in range(0, len(list1)):
            if i < len(list1) - 1 and freq_map[list1[i]] < freq_map[list1[i+1]]:
                total -= freq_map[list1[i]]
            else:
                total += freq_map[list1[i]]
                
        return total


    
