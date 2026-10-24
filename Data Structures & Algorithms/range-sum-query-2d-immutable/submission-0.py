"""
calculate pfix sum 


you want o 1 sum reigon, so you need to get the top subtract it get the left subtract it then add the top left

[[3,]]
"""






class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.pfixSum = []

        for i in range(len(matrix)):
            temp = []
            running = 0
            for j in range (len(matrix[i])):
                if i == 0:
                    running+=matrix[i][j]
                    temp.append(running)
                else:
                    running+=matrix[i][j]
                    x = self.pfixSum[i-1][j]
                    temp.append(running+x)
            self.pfixSum.append(temp)
       

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total = self.pfixSum[row2][col2]

        # Subtract the rectangle above the requested region.
        if row1 > 0:
            total -= self.pfixSum[row1 - 1][col2]

        # Subtract the rectangle left of the requested region.
        if col1 > 0:
            total -= self.pfixSum[row2][col1 - 1]

        # Add back the top-left overlap, which was subtracted twice.
        if row1 > 0 and col1 > 0:
            total += self.pfixSum[row1 - 1][col1 - 1]

        return total


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)