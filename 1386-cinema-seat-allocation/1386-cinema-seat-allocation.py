class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        blocked = defaultdict(set)
        for r, c in reservedSeats:
            if c in [2, 3, 4, 5]:
                blocked[r].add("left")
            if c in [4, 5, 6, 7]:
                blocked[r].add("middle")
            if c in [6, 7, 8, 9]:
                blocked[r].add("right")

        total = 2 * (n - len(blocked))  # untouched rows fit 2 families each
        numaval = {0: 2, 1: 1, 2: 1, 3: 0}  # families still fittable given blocked-block count
        for numb in blocked.values():
            total += numaval[len(numb)]

        return total