class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        total_time = 0
        
        # Using xrange for Python 2 efficiency
        for i in range(len(points) - 1):
            # Current point
            x1, y1 = points[i]
            # Next point
            x2, y2 = points[i + 1]
            
            # Calculate absolute differences
            dx = abs(x2 - x1)
            dy = abs(y2 - y1)
            
            # The time to move between two points is the max of dx and dy
            # because diagonal moves cover both axes simultaneously.
            total_time += max(dx, dy)
            
        return total_time


sol = Solution()
print(sol.minTimeToVisitAllPoints([[1,1],[3,4],[-1,0]]))