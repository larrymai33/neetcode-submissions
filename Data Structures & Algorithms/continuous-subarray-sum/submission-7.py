"""
array nums int k 
true if nums has subarray where sum of subarray is mutliple of k and len > 2

need to check all sub array sums
prefix sum

mutlpe of k exists when there is an integer that multiples by k to get the int
- 



[23,25,29,35,42]

map {}
"""
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        m = {0:-1} #remainder, index


        running = 0


        for i,j in enumerate(nums):
            running +=j

            if running%k in m:
                if i - m[running % k] >=2:
                    return True
            else:
                m[running%k] = i
        
        return False



