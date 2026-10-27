class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        memo = {}
        def recur(row,col):

            if row >= len(triangle)-1 or col > len(triangle[row])-1 or row < 0:
                return triangle[row][col]

            if (row,col) in memo:
                return memo[(row,col)]
            
            else:
                memo[(row,col)] = triangle[row][col] + min(recur(row+1,col), recur(row+1,col+1))
                
            return memo[(row,col)]

        
        return recur(0,0)