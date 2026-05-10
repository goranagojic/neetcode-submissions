class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        squares = [set() for _ in range(9)]

        n_rows, n_cols = len(board), len(board[0])
        print(n_rows)
        print(n_cols)
        for i in range(n_rows):
            for j in range(n_cols):

                num = board[i][j]
                if num == '.':
                    continue
                print(num)

                # row check
                if num in rows[i]:
                    print(rows[i])
                    print("rows")
                    return False
                rows[i].add(num)

                # col check
                if num in cols[j]:
                    print("cols")
                    return False
                cols[j].add(num)

                # square check
                si, sj = i // 3, j // 3
                if num in squares[si*3+sj]:
                    print("squares")
                    return False
                squares[si*3+sj].add(num)

            print(rows[i])

        return True

