
"""
1 + 2 = 3 
2  + (5 + (3-2)) = 8

    i[1] + 
4 + (3 + (8-4)) = 11


add difference 


"""


class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        divisor = len(customers)

        waiting = 0
        deficit = 0

        for i in range(len(customers)):
            if customers[i][0] > deficit:
                waiting += customers[i][1]
                deficit = customers[i][1] + customers[i][0]
                print(deficit)
            else:
                waiting += customers[i][1] + (deficit - customers[i][0])
                deficit = customers[i][1] + (deficit - customers[i][0]) + customers[i][0]

        
        return waiting / divisor
            
            
            

