'''
Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.
'''
class Solution:
    def isValidSudoku(self, board: 'List[List[str]]') -> 'bool':
        rowdup = []
        coldup = {k: [] for k in range(9)}
        subdict = {'00':[],'01':[],'02':[],
                  '10':[],'11':[],'12':[],
                  '20':[],'21':[],'22':[],}
        for i in range(9):
            rowdup.clear()
            for j in range(9):
                if board[i][j] != ".":
                    if board[i][j] not in rowdup:
                        rowdup.append(board[i][j])
                    else:
                        return False
                    subscheck = str(int(i/3)) + str(int(j/3))
                    if board[i][j] not in subdict[subscheck]:
                        subdict[subscheck].append(board[i][j])
                    else:
                        return False
                if board[j][i] != ".":
                    if board[j][i] not in coldup[i]:
                        coldup[i].append(board[j][i])
                    else:
                        print("col")
                        return False
        
        return True
                
            
        
