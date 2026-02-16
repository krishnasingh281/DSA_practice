class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        n = numRows
        for i in range(n):
            templist = []
            for j in range(i+1):
                templist.append(int(self.ncr(i,j)))
            ans.append(templist)

        return ans
        
    def ncr(self, n, r):
        res = 1
        for i in range(0,r):
            res = res*(n-i)
            res = res/(i+1)
        return res