class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        """

        - cant change order of subsequence
        - if already subsequence output is 0
        - worst case = we append entire t string to s to make it a subsequence

        - two pointer technique, where we keep track of both s and t initially
        - when they diverge we increment 
        - when right pointer is done return increment


        """

        sPointer = 0

        tPointer = 0

        ans = 0

        while tPointer < len(t) and sPointer < len(s):
            if t[tPointer] != s[sPointer]:
                sPointer +=1
            else:
                tPointer +=1 
                sPointer +=1
                
        print(tPointer)

        return len(t) - tPointer
            



    