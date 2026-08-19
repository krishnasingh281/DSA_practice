class Solution:
    def maxPairStrength(self, A: list[int]) -> int:
        n, res = len(A), -1
        for i in range(n):
            for j in range(i + 1, n):
                res = max(res, A[i] * A[j] // gcd(A[i], A[j]) ** 2)
        return res