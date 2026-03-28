class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        res = ""

        for i in range(len(s)):

            longi =  self.expand(s,i,i)
            if len(longi) > len(res):
                res = longi

            longi = self.expand(s,i,i+1)
            if len(longi) > len(res):
                res = longi 

        return res


    def expand(self, s, l, r):
        while l>=0 and r<len(s) and s[l] == s[r]:
            l-=1
            r+=1
        
        return s[l+1:r]
         