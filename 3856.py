class Solution:
    def trimTrailingVowels(self, s: str) -> str:
        s_new = s[::-1]
        count = 0
        for i in range(0,len(s)):
            if s_new[i] == 'a':
                count+=1
            elif s_new[i] == 'e':
                count+=1
            elif s_new[i] == 'i':
                count+=1
            elif s_new[i] == 'o':
                count+=1
            elif s_new[i] == 'u':
                count+=1
            else:
                break
        remove = len(s) - count
        s_new = s[:remove]

        return s_new