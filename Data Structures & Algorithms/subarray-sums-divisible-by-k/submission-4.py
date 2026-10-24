class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        
        m = {0:1}

        running = 0
        ans = 0
        for i in nums:
            running += i 

            if running % k  in m:
                ans += m[running%k]
                m[running%k] += 1
            else:
                m[running%k] = 1
        
        return ans