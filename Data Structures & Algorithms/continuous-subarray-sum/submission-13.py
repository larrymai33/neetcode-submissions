"""
prefix sum
hash 

23 2 4 6 7 
23 25 29 35 42


"""




class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        
        running =0 

        m = {0:-1}

        for i,j in enumerate(nums):
            running += j

            if running % k in m:
                if i - m[running% k] >=2:
                    return True
            else:
                m[running % k] = i

        
        return False