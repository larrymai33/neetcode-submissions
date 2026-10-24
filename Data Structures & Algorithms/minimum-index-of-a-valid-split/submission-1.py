class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        """

        whatever number occurs the most has to be n * 2 > len(splitArray)

        minimum index = try from left to right

        split where we have 2 arrays that are effectiley counters (hash table)

        sort counter by values 
        top of counter > len(counter) of both subararays we return true


        """

        length = len(nums)

        domNum, domCount = Counter(nums).most_common(1)[0]


        leftCount = 0
        rightCount = domCount
    
        for i in range(length):
            if nums[i] == domNum:
                leftCount +=1
                rightCount -=1
            leftLen = i + 1
            rightLen = length - leftLen

            if leftCount * 2 > leftLen and rightCount * 2 > rightLen:
                return i
            

        return -1





   
        

