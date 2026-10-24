class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pfix = [1]
        sfix = [1]


        pfixSum = 1
        sfixSum = 1

        for i in nums:
            pfixSum *= i

            pfix.append(pfixSum)
        
        for i in range(len(nums)-1, -1, -1):
            sfixSum *= nums[i]
            sfix.append(sfixSum)
        
       # print(pfix)
        #print(sfix)

        ans = []
        j = 0

        for i in range(len(nums)-1, -1, -1):
            ans.append(sfix[i] * pfix[j])
            j+=1
        
        return ans


