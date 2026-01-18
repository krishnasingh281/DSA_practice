class Solution(object):
    def maxMatrixSum(self, matrix):
        total = 0
        negative_count = 0
        smallest_absolute_value = float('inf')

        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[0])):
                total = total + abs(matrix[i][j])
                if matrix[i][j] < 0:
                    negative_count += 1
                smallest_absolute_value = min(smallest_absolute_value, abs(matrix[i][j]))

        if negative_count % 2 == 1:
            total -= 2 * smallest_absolute_value

        return total
# Example usage:
solution = Solution()   
matrix = [[1,-1],[-1,1]]
result = solution.maxMatrixSum(matrix)
print(result)  # Output the result


        
