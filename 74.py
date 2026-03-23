class Solution(object):
    def searchMatrix(self, matrix, target):
        if not matrix or not matrix[0]:
            return False
            
        rows = len(matrix)
        cols = len(matrix[0])
        
        lo, hi = 0, (rows * cols) - 1
        
        while lo <= hi:
            mid = (lo + hi) // 2
            mid_value = matrix[mid // cols][mid % cols]
            
            if mid_value == target:
                return True
            elif mid_value < target:
                lo = mid + 1
            else:
                hi = mid - 1
                
        return False