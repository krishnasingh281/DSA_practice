class Solution(object):
    def plusOne(self, digits):
        if digits is None or len(digits) == 0:
            return digits
        
        if digits[-1] < 9:
            digits[-1] += 1
            return digits

        # Handle the case where the last digit is 9
        digits[-1] = 0
        for i in range(len(digits) - 2, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0

        return [1] + digits
    
