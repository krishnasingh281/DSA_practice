class Solution:
    def rearrangeString(self, s: str, x: str, y: str) -> str:
        a=[]
        b=[]
        mid=[]
        for ch in s:
            if ch==y:
                b.append(ch)
            elif ch==x:
                a.append(ch)
            else:
                mid.append(ch)
        return "".join(b+mid+a)