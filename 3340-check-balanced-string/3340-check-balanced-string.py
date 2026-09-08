class Solution:
    def isBalanced(self, num: str) -> bool:
        esum = 0
        osum = 0
        for i in range(len(num)):
            if i %2 == 0:
                esum += int(num[i])
            else:
                osum += int(num[i])
        return esum == osum