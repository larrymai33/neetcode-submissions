


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        ans = []

        nums.sort()

        for i in range(len(nums)- 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left = i+1
            right = len(nums)-1
            temp = []
            while left < right:
                if left != i or right != i and left != right:
                    if nums[left] + nums[i] + nums[right] == 0:
                        temp.append(nums[left])
                        temp.append(nums[i])
                        temp.append(nums[right])
                        right-=1
                        left +=1
                        ans.append(temp)
                        temp = []
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                    elif nums[left] + nums[i] + nums[right] > 0:
                        right -=1
                    else:
                        left +=1 
            temp.sort()
            if temp not in ans and temp:
                ans.append(temp)
        
        return ans
                
