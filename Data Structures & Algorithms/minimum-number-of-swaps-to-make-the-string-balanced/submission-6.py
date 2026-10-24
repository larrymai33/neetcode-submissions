"""

min swaps int

string, contains length of n/2 opening brackets n/2 closing brackets 

amount of opening and closing is same

stack, when you see closing mark it for swap, when you see open, close the closing pop from stack and then inc count as a swap

if we see closing, append to stack, 

doesnt work

"""

class Solution:
    def minSwaps(self, s: str) -> int:
        ans = 0
        maxi = 0

        for i in s:
            if i == "[":
                ans -=1
            else:
                ans +=1
            maxi = max(maxi, ans)

        return (maxi + 1) //2
