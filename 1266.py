class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        total_time = 0
        
        
        for i in range(len(points) - 1):
            # Current point
            x1, y1 = points[i]
            # Next point
            x2, y2 = points[i + 1]
            
            # Calculate absolute differences
            dx = abs(x2 - x1)
            dy = abs(y2 - y1)
            
            # The time to move between two points is the max of dx and dy

            total_time += max(dx, dy)
            
        return total_time

