class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if not s:
            return 0
        
        sign = 1
        i = 0
        
        if s[i] == '-':
            sign = -1
            i += 1
        elif s[i] == '+':
            i += 1
            
        result = 0
        MAX_INT = 2147483647
        MIN_INT = -2147483648
        
        while i < len(s) and s[i].isdigit():
            result = result * 10 + int(s[i])
            
            if sign * result >= MAX_INT:
                return MAX_INT
            if sign * result <= MIN_INT:
                return MIN_INT
            i += 1
            
        return sign * result
