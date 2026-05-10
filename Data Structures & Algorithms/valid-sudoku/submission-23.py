class Solution:

    class Sudoku:

        def __init__(self, board: List[List[str]]):
            self.col_len = len(board) # rows
            self.row_len = len(board[0]) # cols

            self.board = board
            print(self.board)

        def has_duplicates(self, arr: List[str]):
            just_digits = set()
            
            for symbol in arr:
                if symbol == ".":
                    continue
                if symbol in just_digits:
                    return True
                just_digits.add(symbol)

            return False

        def has_duplicates_col(self, idx: int) -> bool:
            # assemble column
            column = ['.'] * self.col_len
            for i in range(0, self.col_len):
                column[i] = self.board[i][idx]

            # check duplicates
            return self.has_duplicates(column)

        def has_duplicates_row(self, idx: int) -> bool:
            row = self.board[idx]
            return self.has_duplicates(row)
            
        def _get_square(self, row_idx, n_rows, col_idx, n_cols):
            """todo"""
            flattened_subboard = []
            for i in range(row_idx, row_idx+n_rows, 1):
                flattened_subboard.extend(self.board[i][col_idx:col_idx+n_cols])
            
            return flattened_subboard

        def has_duplicates_square(self, row_idx, n_rows, col_idx, n_cols):

            square_f = self._get_square(row_idx, n_rows, col_idx, n_cols)
            print(square_f)
            
            return self.has_duplicates(square_f)
                

    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # for 9 rows, check all rows for: value span, duplicates
        # for 9 cols, check all cols for: value span, duplicates
        # for 9 cols, check all cols for; value span duplicates

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
        