class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        """
        1. compute prefix sum per each element
        2. divide prefixsum + each nums by k 
        3. increment each time from step 2 that number is found divide by k


        """

        n, res = len(nums), 0

        for i in range(n):
            curSum = 0
            for j in range(i, n):
                curSum += nums[j]
                if curSum % k == 0:
                    res += 1

        return res
        



