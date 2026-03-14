class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
    
        # The elegant trick
        return goal in (s + s)