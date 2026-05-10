class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        # do padding
        rows, cols = len(matrix), len(matrix[0])
        self.matrix = [[0 for _ in range(0, cols+1)] for j in range(0, rows+1)]

        # add elements of the input matrix
        for i in range(1, rows+1):
            for j in range(1, cols+1):
                self.matrix[i][j] = matrix[i-1][j-1]

        self.cols, self.rows = len(self.matrix[0]), len(self.matrix)
        
        print("------------")
        for i in range(rows+1):
            print(self.matrix[i])
        print("------------")

        # calculate prefix sums
        for i in range(1, rows+1):
            for j in range(1, cols+1):
                self.matrix[i][j] = self.matrix[i][j-1] + self.matrix[i][j] + self.matrix[i-1][j]-self.matrix[i-1][j-1]
        
        print("------------")
        for i in range(self.rows):
            print(self.matrix[i])
        print("------------")
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # constraint: must work in O(1) time complexity
        # (row1, col1) - coordinates of the rectangle upper left corner
        # (row2, col2) - coordinates of the lower right corner
        # how to calculate (row2,col2)-(row1,col2)-(row2,col1)-(row1,col1)
        
        return self.matrix[row2+1][col2+1] - self.matrix[row1][col2+1] - self.matrix[row2+1][col1] + self.matrix[row1][col1]
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)