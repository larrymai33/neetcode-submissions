class NumMatrix:


    def __init__(self, matrix: List[List[int]]):

        self.pMatrix = []
        
        for i in range(len(matrix)):
            temp = []
            running = 0
            for j in range(len(matrix[i])):
                if i == 0:
                    running += matrix[i][j]
                    temp.append(running)
                else:
                    running += matrix[i][j]
                    temp.append(running + self.pMatrix[i-1][j])
            self.pMatrix.append(temp)


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total = self.pMatrix[row2][col2]

        if row1 > 0:
            total -= self.pMatrix[row1-1][col2]

        if col1 > 0:
            total -= self.pMatrix[row2][col1 -1]
        
        if row1 > 0 and col1 > 0:
            total += self.pMatrix[row1 - 1][col1 - 1]
        
        return total

        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)