class Solution:
    def minDays(self, bloomDay: list[int], m: int, k: int) -> int:
        if m * k > len(bloomDay):
            return -1
            
        def is_possible(day):
            bouquets = 0
            flowers = 0
            for bloom in bloomDay:
                if bloom <= day:
                    flowers += 1
                    if flowers == k:
                        bouquets += 1
                        flowers = 0
                        if bouquets >= m: return True
                else:
                    flowers = 0
            return bouquets >= m

        low, high = min(bloomDay), max(bloomDay)
        while low <= high:
            mid = (low + high) // 2
            if is_possible(mid):
                high = mid - 1
            else:
                low = mid + 1
        
        return low