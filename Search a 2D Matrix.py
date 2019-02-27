'''
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
'''
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        rows = len(matrix)
        columns = len(matrix[0])
        trow = 0
        for i in range(rows):
            if target>=matrix[i][0]:
                trow = i
        if target in matrix[trow]:
            return True
        else:
            return False
