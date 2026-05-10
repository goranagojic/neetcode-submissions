class Solution:

    class Sudoku:

        def __init__(self, board: List[List[str]]):
            self.col_len = len(board)       # rows
            self.row_len = len(board[0])    # cols
            self.board = board

        def has_duplicates(self, arr: List[str]):
            """generic function to check for duplicates in the array"""
            # time complexity O(g) bounded by O(n) where n is array length - basically constant in this case since n is always 9. so O(1)
            # space complexity O(n)
            just_digits = set()
            
            for symbol in arr:
                if symbol == ".":
                    continue
                if symbol in just_digits:
                    return True
                just_digits.add(symbol)

            return False

        def has_duplicates_col(self, idx: int) -> bool:
            """checks duplicates in a the column by first assembling the column and than invoking the function to find duplicates."""
            # time complexity O(n) - basically constant since n is always 9
            # assemble column
            column = ['.'] * self.col_len
            for i in range(0, self.col_len):
                column[i] = self.board[i][idx]

            # check duplicates
            # O(1) in this context for the same reason
            return self.has_duplicates(column)

        def has_duplicates_row(self, idx: int) -> bool:
            """checks duplicates in a the row by first assembling the row and than invoking the function to find duplicates"""
            # O(1)
            row = self.board[idx]
            # O(1)
            return self.has_duplicates(row)
            
        def _get_square(self, row_idx, n_rows, col_idx, n_cols):
            """todo"""
            # again O(n) -> O(1)
            flattened_square = []
            for i in range(row_idx, row_idx+n_rows, 1):
                flattened_square.extend(self.board[i][col_idx:col_idx+n_cols])
            
            return flattened_square

        def has_duplicates_square(self, row_idx, n_rows, col_idx, n_cols):
            # time complexity same as above
            square_f = self._get_square(row_idx, n_rows, col_idx, n_cols)
            print(square_f)
            
            return self.has_duplicates(square_f)
                

    def isValidSudoku(self, board: List[List[str]]) -> bool:

        sudoku_board = self.Sudoku(board)

        # check rows for duplicates
        for row_idx in range(0, 9, 1):
            if sudoku_board.has_duplicates_row(row_idx):
                return False # board not valid

        # check cols for duplicates
        for col_idx in range(0, 9, 1):
            if sudoku_board.has_duplicates_col(col_idx):
                return False # board not valid

        for row_idx in [0, 3, 6]:
            for col_idx in [0, 3, 6]:
                if sudoku_board.has_duplicates_square(row_idx, 3, col_idx, 3):
                    return False
        
        return True
        