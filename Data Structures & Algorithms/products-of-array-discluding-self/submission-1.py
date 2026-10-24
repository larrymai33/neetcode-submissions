class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pfix = [1]
        sfix = [1]


        runningP = 1
        runningS = 1

        for i in nums:
            runningP *= i
            pfix.append(runningP)
        

        for i in range((len(nums) - 1), -1, -1):
            runningS *= nums[i]
            sfix.append(runningS)
        
        ans = []

        j = 0

        for i in range((len(nums) - 1), -1, -1):
            ans.append(sfix[i] * pfix[j])
            j+=1
        
        return ans


