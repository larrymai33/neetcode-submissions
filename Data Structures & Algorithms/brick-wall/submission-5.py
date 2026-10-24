"""
rows share heights
- rows must share one common value with i + 1 rows i -1 rows



"""


class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        
        m = defaultdict(int)

        length = len(wall)

        for i in range(len(wall)):
            running = 0
            for j in range(len(wall[i])-1):
                running += wall[i][j]
                m[running] += 1
        
        maxi = 0

        ans = 0 
        if not m:
            for row in wall:
                ans +=1
        
        if not m:
            return ans

        for i in m.values():
            maxi = max(i,maxi)
        
  

        return length - maxi


            


        

