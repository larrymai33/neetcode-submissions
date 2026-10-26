class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        memo = {}
        
        def recur(i, prev):

            if i == len(nums):
                return 0
            else:


                if (i,prev) in memo:
                    return memo[(i,prev)]
                else:
                    take = 0
                    if prev == -1 or nums[i] > nums[prev]:
                        take = 1 + recur(i+1, i)
                    memo[(i,prev)] = max(recur(i+1,prev), take)

                #give = recur(i+1,length)
                #take = recur(i+1,length+1)
                #if currNum > take:
                    #take = 0
                
                return memo[(i,prev)]
        
        return recur(0,-1)



            