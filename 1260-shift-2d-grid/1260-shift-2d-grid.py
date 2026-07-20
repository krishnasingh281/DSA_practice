class Solution:
    def shiftGrid(self, g, k):
        m, n = len(g), len(g[0])

        k = k%(m*n)
        if k == 0: return g # no change

        r = k//n
        g = g[m-r:] + g[:m-r]  # shift rows by r

        c = k%n
        if c == 0: return g  # early return if k % n == 0 (no col shift needed)

        return [ g[i-1][n-c:] + g[i][:n-c] for i in range(m) ] # shift each column by c