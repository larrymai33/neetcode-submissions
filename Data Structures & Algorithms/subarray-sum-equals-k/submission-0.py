"""
all combinations that add up to K
prefixsum
"""


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixArr = [0]
        hashm = {0:1}
        running = 0
        ans = 0

        for i in nums:
            running += i

            if running - k in hashm:
                ans+=hashm[running-k]
            if running in hashm:
                hashm[running] += 1
            else:
                hashm[running] = 1
        
        return ans

            
