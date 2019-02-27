'''
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.
'''
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        columns =len(matrix[0])
        def row(currcolumn):
            for i in range(rows):
                if matrix[i][currcolumn] != 0:
                    matrix[i][currcolumn] = 'a'
        def column(currrow):
            for i in range(columns):
                if matrix[currrow][i] != 0:
                    matrix[currrow][i] = 'a'
        for i in range(rows):
            for j in range(columns):
                if matrix[i][j] == 0:
                    column(i)
                    row(j)
        for i in range(rows):
            for j in range(columns):
                if matrix[i][j] == 'a':
                    matrix[i][j] = 0
