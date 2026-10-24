

class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:

        left = 0
        cost = 0

        ans = 0
        for i in range(len(s)):          
            tempcost = (abs(ord(s[i]) - ord(t[i])))
            cost += tempcost
            while cost > maxCost:
                cost -= (abs(ord(s[left]) - ord(t[left])))
                left += 1
            ans = max(i-left+1,ans)
        
        return ans
            

