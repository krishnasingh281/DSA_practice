class Solution:
    def totalFruit(self, fruits: List[int]) -> int:

        low = 0
        result = 0
        buckets = 2

        freq = {}

        for high in range(len(fruits)):

            freq[fruits[high]] = freq.get(fruits[high], 0) + 1

            while len(freq) > buckets:

                freq[fruits[low]] -= 1

                if freq[fruits[low]] == 0:
                    del freq[fruits[low]]

                low += 1

            result = max(result, high - low + 1)

        return result