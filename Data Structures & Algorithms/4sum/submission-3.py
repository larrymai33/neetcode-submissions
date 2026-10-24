

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        nums.sort()

        left = 1
        right = len(nums) -2

        poop = 0
        pee = len(nums) - 1

        ans = []


        for i in range(len(nums)):
            for j in range(len(nums)-1, 0, -1):
                left = i+1
                right = j-1
                while left < right:
                    if (nums[left] + nums[right] + nums[i] + nums[j]) == target:
                        if [nums[left], nums[right], nums[i] , nums[j]] not in ans:
                            ans.append([nums[left], nums[right], nums[i] , nums[j]])
                        left +=1 
                        right -=1
                    elif nums[left] + nums[right] + nums[i] + nums[j] < target:
                        left +=1
                    else:
                        right -=1
        
        return ans


