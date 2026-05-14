class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        # arbitrary time complexity
        # matrix may not be rectangular
        # time complexity O(nm) - quadric when n and m are similar
        
        self.matrix = [row[:] for row in matrix]


        # cumulative sum matrix - first cum sum rows
        # time complexity: m x (n-1) - m number of rows, n cols
        for i in range(0, len(matrix)):               # iterates rows
            for j in range(1, len(matrix[0])):        # iterates cols
                matrix[i][j] += matrix[i][j-1]
                
        # now calculate cum sum for rectangles
        # time complexity: n
        for j in range(0, len(matrix[0])):
            self.matrix[0][j] = matrix[0][j]

        # time complexity: (m-1)xn
        for i in range(1, len(matrix)):
            for j in range(0, len(matrix[0])):
                if j != 0:
                    self.matrix[i][j] += matrix[i][j-1]
                self.matrix[i][j] += self.matrix[i-1][j]    
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # must be O(1) time, i.e. must have the exactly same number of operations executed regardless of rectangle size

        s22 = self.matrix[row2][col2]
        s12 = self.matrix[row1-1][col2]   if row1 > 0 else 0
        s21 = self.matrix[row2][col1-1]   if col1 > 0 else 0
        s11 = self.matrix[row1-1][col1-1] if row1 > 0 and col1 > 0 else 0

        return s22 - s21 - s12 + s11
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)