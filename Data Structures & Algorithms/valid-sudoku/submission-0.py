class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        def isValidHelper(board, i, j):
            val = board[i][j]

            # Check in Rows
            for k in range(9):
                if k != j and board[i][k] == val:
                    return False
            # Check in Cols
            for k in range(9):
                if k != i and board[k][j] == val:
                    return False

            boxRow = i-(i%3)
            boxCol = j-(j%3)
            for m in range(boxRow, boxRow+3):
                for n in range(boxCol, boxCol+3):
                    if (m != i or n != j) and board[m][n] == val:
                        return False
            return True
        
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    if not isValidHelper(board, i, j):
                        return False
        return True