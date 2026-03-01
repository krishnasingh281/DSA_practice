class Solution:
    def reverseBits(self, n):

        binary = f"{n:032b}"
        reversed_binary = binary[::-1]

        return int(reversed_binary, 2)