class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        m = {0 : 1}

        ans = 0
        running = 0

        for i in nums:
            running += i
            if running -k in m:
                ans += m[running-k]
            if running  in m:
                m[running] +=1
            else:
                m[running] = 1
        return ans