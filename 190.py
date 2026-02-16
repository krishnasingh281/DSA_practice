class Solution:
    def reverseBits(self, n: int) -> int:

        binary = f"{n:032b}"
        reversed_binary = binary[::-1]
    
        # 3. Convert that reversed string back to an integer (Base 2)
        return int(reversed_binary, 2)