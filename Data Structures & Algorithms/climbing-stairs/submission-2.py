class Solution:
    def climbStairs(self, n: int) -> int:

        memo = {}
        
        def recur(i):

            if i == 1:
                return 1
            if i == 2:
                return 2
            if i == 3:
                return 3
            else:
                if i in memo:
                    return memo[i]
                else:
                    memo[i] = recur(i-1) + recur(i-2)
                
                return memo[i]

        
        return recur(n)

