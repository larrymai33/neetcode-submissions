class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        """

        prefix sum

        1 + 3 + 5

        1 4 9 

        """

        prefixsumarr = [0]
        count = 0
        m = {}
        ans = 0

        for i in arr:
            count += i
            x = i - count
            prefixsumarr.append(count)

        even = 0
        odd = 0

        for i in prefixsumarr:
            if i % 2 == 0:
                even += 1
            else:
                odd += 1
            
        return even * odd
        



        


        