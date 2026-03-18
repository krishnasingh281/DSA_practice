import math
from typing import List

class Solution:
    def isprime(self, n: int) -> bool:
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(math.isqrt(n)) + 1, 2):
            if n % i == 0:
                return False
        return True   

    def checkPrimeFrequency(self, nums: List[int]) -> bool:
        freq_map = {}
        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1

        # FIX: check if ANY frequency is prime
        for frequency in freq_map.values():
            if self.isprime(frequency):
                return True
        
        return False