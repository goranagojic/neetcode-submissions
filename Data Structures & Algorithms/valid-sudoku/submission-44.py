class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        squares = [set() for _ in range(9)]

        n_rows, n_cols = len(board), len(board[0])
        for i in range(n_rows):
            for j in range(n_cols):

                num = board[i][j]
                if num == '.':
                    continue

                # row check
                if num in rows[i]:
                    return False
                rows[i].add(num)

                # col check
                if num in cols[j]:
                    return False
                cols[j].add(num)

                # square check
                si, sj = i // 3, j // 3
                if num in squares[si*3+sj]:
                    return False
                squares[si*3+sj].add(num)

        return True

