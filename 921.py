class Solution:
    def minAddToMakeValid(self, s):

        dial1 = 0
        dial2 = 0

        for char in s:
            if char == '(':
                dial1 += 1

            elif char == ")" and dial1 != 0:
                dial1 -= 1

            else:
                dial2 += 1

        return dial1 + dial2
        